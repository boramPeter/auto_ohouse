from multiprocessing import Process
import os, time, subprocess, sys
# from app.common.app_config.data import WdaPath
from app.common.base_method.read_dict_result import IosReadDictResult
from app.common.app_config.data import PicklePath,UDID
from app.common.app_config.data import BddFeaturePath
from app.common.base_method.ios_result_binary import Result
# import concurrent.futures
from report.create_report import AppCreateSlackReport
# import threading
# from datetime import datetime
# from app.common.base_method.ios_remote_control_func import request_wda_run,request_wda_stop,request_wda_del
from report.goole_spread_sheet_func.make_spread_sheet_func import execute_parallel_copy
from report.slack_webhook import SlackWebhook
from flask_active.test_running_check.running_value_provider import get_terminate_value,send_test_running_terminate_value
# from report.testrail_func.festrail_api import create_test_runs,delete_test_run
import argparse

wda_1_running = False
wda_2_running = False
wda_3_running = False
behave_running = False


def run_behave(main_features, tags, debug=None):
    Result().write_result("test_execution", tags)
    Result().write_result("test_execution_debug", "True") if debug is not None else Result().write_result("test_execution_debug", "False")
    feature_files = [
        f"{BddFeaturePath.ios_bdd_path}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags={tags}"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )

    return result.returncode


def run_behave2(main_features, test_execution,tags,debug=None):

    if debug is not True:
        execute_parallel_copy("iOS", test_execution)


    feature_files = [
        f"{BddFeaturePath.ios_bdd_path2}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags={tags}"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )
    return result.returncode

def run_behave3(main_features, tags):

    feature_files = [
        f"{BddFeaturePath.ios_bdd_path3}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags={tags}"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )
    return result.returncode
#

def to_none(val: str | None) -> str | None:
    if val is None:
        return None
    if str(val).strip().lower() == 'none' or str(val).strip() == '':
        return None
    return val
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('true', 't', '1'):
        return True
    elif v.lower() in ('false', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean 값은 True 또는 False로 입력해야 합니다.')
def main_ios(test_execution, debug=None,service=None,user_id=None,version=None):
    global wda_1_running, wda_2_running, wda_3_running

    os.environ["IOS_AUTO_FLAG"] = "0"
    if test_execution == "ST":
        tags = "@PRE,@ST"
        test_run = "ST"
    elif test_execution == "RT":
        tags = "@PRE,@ST,@RT"
        test_run = "RT"
    else:
        tags = "@PRE,@ST"
        test_run = "ST"


    if service is None:

        main_features = [
            "pre_condition"
        ]
    else:
        main_features = ["pre_condition", service]
        tags = "@PRE,@ST,@개별" if test_run == "ST" else "@PRE,@ST,@RT,@개별"

    if debug:
        tags += ",@True"

    try:
        os.remove(PicklePath.ios_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")
    Result().write_result("is_ios_running", "true")
    if version is not None:
        from flask_active.version_func import _save_request_text_to_binary
        _save_request_text_to_binary(version,"iOS")

    processes = []

    process_behave = Process(target=run_behave, args=(main_features, tags, debug))
    process_behave2 = Process(target=run_behave2, args=(main_features, test_execution,tags,debug))
    process_behave3 = Process(target=run_behave3, args=(main_features, tags))

    processes.append(process_behave)
    processes.append(process_behave2)
    processes.append(process_behave3)

    for process in processes:
        process.start()

    for process in processes:
        process.join()



    if Result().read_result_slack(
        "is_ios_running") == "false":
        SlackWebhook().start_slack_msg(f"아이폰 자동화 테스트가 중단되었습니다. 테스트 수행 로그를 확인해주세요")
    elif debug is not True and Result().read_result_slack("iOS_spreadsheet") == "":
        SlackWebhook().start_slack_msg(f"스프레드시트 생성에 실패하여 테스트 강제종료.")

    elif get_terminate_value("ios") == True:
        SlackWebhook().start_slack_msg("아이폰 자동화 테스트가 강제종료 되었습니다.")
    else:
        print(f"리포팅 전 플래그 체크 {test_execution,debug,service}")
        IosReadDictResult().execute_read_dict_result(test_execution, debug=debug,individual=service,user_id=user_id)

    data_payload = {
        "ios_terminate": False
    }
    send_test_running_terminate_value(data_payload)

    os.remove(PicklePath.ios_pickle_path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_execution', default="RT", help='실행 모드 (기본: RT)')
    parser.add_argument('--debug', type=str2bool, default=True, help='디버그 모드 (True 또는 False)')
    parser.add_argument('--service', type=str, default=None, help='서비스 이름 ("pre_condition")')
    parser.add_argument('--user_id', default=None, help='유저 ID (선택)')
    parser.add_argument('--version', default=None,help='수동 버전 생성용')


    args = parser.parse_args()

    service = to_none(args.service)
    user_id = to_none(args.user_id)
    version = to_none(args.version)

    main_ios(
        test_execution=args.test_execution,
        debug=args.debug,
        service=service,
        user_id=user_id,
        version=version
    )
