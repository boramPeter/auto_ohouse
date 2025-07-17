import pickle
import re, os
import threading
from flask import Flask
from flask import request
from flask import make_response
from flask import json,jsonify
from report.slack_webhook import SlackWebhook
#from app.common.base_method.version_binary import VersionBinary
from app.ios.testcase.ios_testrunner_bdd import main_ios
from app.android.testcase.aos_testrunner_bdd import main_aos
from web.test_runner import main_web
from flask_active.jenkins_trigger import jenkins_trigger, jenkins_job_checker
from flask_active.parallel_runner import run_parallel, run_parallel_process
from flask_active.jira_formatter import extract_os_version
from flask_active.github_pull import git_checkout_rebase_main
from app.common.app_config.data import AppVersion
from crontab import CronTab
from datetime import datetime, timedelta
from production.common.method.log_to_slack_func import ReadDictResult
from production.app.ios.prod_ios_testrunner_bdd import main_ios_prod
from production.app.android.prod_aos_testrunner_bdd import main_aos_prod
from production.web.prod_web_testrunner_bdd import main_web_prod
from app.api.Jira.jira_api import JiraApi
from app.api.report.del_block import BlockDeleteClass
from ozipsa.ozipsa_run import run_ozipsa_tc, check_ozipsa_prd
from flask_cors import CORS
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.aos_result_binary import ResultAndroid
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

CORS(app)

ozipsa_run_flag = False
ozipsa_current_request_count = 0
ozipsa_max_request = 4
ozipsa_lock = threading.Lock()


is_aos_running = False
is_ios_running = False
is_web_running = False

android_terminate = False
ios_terminate = False
web_terminate = False

notified_builds = set()

trigger_list = []

def start_msg():
    cron = CronTab(user=True)
    job = cron[0]
    job.minute.on(0)
    job.hour.on(6)
    cron.write()
    SlackWebhook().start_slack_msg("Flask restart complete")


@app.route('/slack_event', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    else:
        return make_response("ok", 200, {"content_type": "application/json"})




'''
?os=and
?os=ios
?os=web
'''
@app.route('/stop_automation', methods=['GET'])
def stop_automation():
    os_param = request.args.get('os')  # GET 파라미터에서 'os' 값을 가져옴
    if os_param == 'and':
        SlackWebhook().start_slack_msg(f"안드로이드 테스트 종료가 실행되었습니다. 완료 메세지를 기다려주세요.")
        _set_global_variables("aOS", True,auto_stop=True)
        return make_response("안드로이드 테스트 종료가 실행되었습니다", 200, {"content-type": "application/json"})
    elif os_param == 'ios':
        SlackWebhook().start_slack_msg(f"아이폰 테스트 종료가 실행되었습니다. 완료 메세지를 기다려주세요.")
        _set_global_variables("iOS", True,auto_stop=True)
        return make_response("아이폰 테스트 종료가 실행되었습니다", 200, {"content-type": "application/json"})
    elif os_param == 'web':
        SlackWebhook().start_slack_msg(f"웹 테스트 종료가 실행되었습니다. 완료 메세지를 기다려주세요.")
        _set_global_variables("web", True,auto_stop=True)
        return make_response("아이폰 테스트 종료가 실행되었습니다", 200, {"content-type": "application/json"})
    else :
        return make_response("파라미터가 없어서 실행되지 않았습니다.", 200, {"content-type": "application/json"})

##################### 커맨드 명령어 ##############################
slack_user_id = None
from flask_active.slack_command.modal import *

@app.route('/eng_qa', methods=['POST'])
def command_qa():
    trigger_id = request.form.get('trigger_id')
    send_modal(trigger_id, eng_qa_modal)
    return make_response("eng-qa에서 사용하는 명령어 반환완료.", 200, {"content-type": "application/json"})


@app.route('/auto_test', methods=['POST'])
def automation_test():
    global slack_user_id
    trigger_id = request.form.get('trigger_id')
    slack_user_id = request.form.get('user_id')
    send_modal(trigger_id, start_automation_modal)
    return make_response("자동화 테스트 시작", 200, {"content-type": "application/json"})

@app.route('/interactive', methods=['POST'])
def interactive():
    global slack_user_id
    payload = json.loads(request.form['payload'])
    event_type = payload['type']
    callback_id = payload['view']['callback_id']
    block_id_1 = payload['view']['blocks'][0]['block_id']

    if event_type == "view_submission":
        if callback_id == "start_automation_modal":
            selected_platform = \
            payload['view']['state']['values']['platform_block']['platform_select']['selected_option']['value']
            if selected_platform in ["android", "ios", "web"]:
                print(selected_platform, slack_user_id)
                default_blocks = automation_option["blocks"].copy()
                try:
                    option = individual_execution_options[selected_platform]
                    automation_option["blocks"].append(option)
                    return jsonify({"response_action": "update", "view": automation_option})
                finally:
                    automation_option["blocks"] = default_blocks.copy()

        if callback_id == "automation_option":
            platform = payload["view"]["blocks"][4]["text"]["text"]
            version = payload['view']['state']['values']['version_block']['version_input']['value']
            debugging = payload['view']['state']['values']['debugging_block']['debugging_select']['selected_option'][
                'value']
            execution = payload['view']['state']['values']['execution_block']['execution_select']['selected_option'][
                'value']
            individual_execution = \
                payload['view']['state']['values']['individual_execution_block']['individual_execution_select'][
                    'selected_option']['value']
            auto_start = \
            payload['view']['state']['values']['auto_start_opt']['auto_start_opt_select']['selected_option']['value']

            # 디버그 True면서 서비스가 all이 아닌경우에만 -> 디버깅 조건만 체크
            slack_user_id = slack_user_id if debugging else None
            print(f"Platform: {platform}")
            platform = (
                "web" if "웹" in str(platform) else
                "aOS" if "안드로이드" in str(platform) else
                "iOS" if "아이폰" in str(platform) else
                "web"
            )
            if auto_start == "auto_stop":
                os_param = (
                    "web" if platform == "web" else
                    "and" if platform == "aOS" else
                    "ios" if platform == "iOS" else
                    "web"
                )

                url = f'http://localhost:5002/stop_automation?os={os_param}'
                requests.get(url)
                return jsonify({"response_action": "clear"})

            individual_execution = None if individual_execution == "all" else individual_execution
            _save_request_text_to_binary(version, platform) if version is not None else del_version(platform)
            debugging = True if debugging == "디버깅" else False
            url = "http://localhost:5002/start_automation"
            data = {
                "platform": platform,
                "execution": execution,
                "debug": debugging,
                "service": individual_execution,
                "user_id": slack_user_id
            }

            requests.post(url, json=data)
            app.logger.info(f"_start_automation 시작 {platform}, {execution}, {debugging}, {individual_execution}, {slack_user_id}")
            slack_user_id = None
            return jsonify({"response_action": "clear"})

        if callback_id == "eng_qa_modal":
            command = payload['view']['state']['values']['eng_qa_block']['command_select']['selected_option']['value']
            if command == "help":
                return jsonify({"response_action": "update", "view": command_list})
            else:
                modal = url_return(command)
                print(modal, command)
                return jsonify({"response_action": "update", "view": modal})
        if block_id_1 == "report_block":
            reporter_user_id = payload['view']['state']['values']['report_block']['id_input']['value']
            BlockDeleteClass().del_block(reporter_user_id)
            return jsonify({"response_action": "clear"})

    return jsonify({"status": "ignored"})
##################### 커맨드 명령어 ##############################

@app.route('/start_automation', methods=['POST'])
def start_automation():
    data = request.get_json()
    platform = data.get("platform")
    execution = data.get("execution")
    debug = data.get("debug")
    user_id = data.get("user_id")
    if debug != True:
        debug = None
        user_id = None
    service = data.get("service")

    return _start_automation(platform, execution, debug=debug, service=service, user_id=user_id)






'''
!!!! check !!!!
'''

def _start_automation(platform,test_execution,auto_trigger=None,debug=None,service=None,user_id=None):
    global is_ios_running, is_aos_running, is_web_running, trigger_list
    app.logger.info(f"_start_automation 시작 : {platform},{test_execution},is_web_running:{is_web_running},auto_trigger:{auto_trigger},{debug},{service},{user_id},trigger_list:{trigger_list}")


    '''
            보안을 위해 일부만 남김
            '''
    app.logger.info(f"트리거 실행 전 {job_name},{platform},{test_execution},{debug},{service},{user_id},{version}")

    jenkins_trigger(job_name=job_name,test_execution=test_execution_args,debug=debug, service=service, user_id=user_id,version=version)


    return response



if __name__ == '__main__':
    # start_msg()
    HOST = '0.0.0.0'
    PORT = 5002
    app.run(host=HOST, port=PORT, debug=False)
