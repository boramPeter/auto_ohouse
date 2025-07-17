from report.slack_webhook import SlackWebhook
from app.common.app_config.data import PicklePath
from report.read_dict_result import WebReadDictResult
import subprocess, os
from report.goole_spread_sheet_func.make_spread_sheet_func import execute_parallel_copy
from flask_active.test_running_check.running_value_provider import get_terminate_value, \
    send_test_running_terminate_value
# from report.testrail_func.festrail_api import create_test_runs, delete_test_run
# from web.BasicSetting.web_result_binary import ResultWeb
import argparse


def return_service_str(service):
    service_str = service
    if service == "comm_s":
        service_str = "comm_service"
    elif service == "comm_p":
        service_str = "comm_platform"

    return service_str


def run_pytest(execution, debug=None, service=None, test_execution=None):
    marker_command = "test" if execution == "temporary" else "smoke or regression" if execution == "regression" else execution
    working_directory = os.getcwd()
    parts = working_directory.split(os.sep)
    try:
        workspace_index = parts.index("workspace")
        jenkins_target_directory = os.sep.join(parts[:workspace_index + 2])
    except Exception:
        index = working_directory.rfind("ohs-qa-automation")
        target_directory = working_directory[:index + len("ohs-qa-automation")]
        jenkins_target_directory = target_directory
        print("app_config/data: 젠킨스 환경에서의 예외처리")



    # 진행 서비스 선정
    if service is not None:
        if service == "ohsweb":
            main_features = ["common", "home", "o2o", "search"]
        elif service == "COMMWEB":
            main_features = ["comm_service", "comm_platform", "claim", "payment"]
        elif service == "CONTWEB":
            main_features = ["home", "common","community","content","affiliate"]
        else:
            main_features = [service]  # lifestyle, payment, 그 외 개별실행
    else:
        main_features = ["common", "home", "o2o", "search", "comm_service", "comm_platform", "claim","community","content","affiliate",
                         "payment"]

    # 결과시트 생성 여부 결정 (debug가 아니라면 무조건 시트 생성함)
    # 250211) payment 테스트의 경우 시트 생성하지 않도록 수정 (FTC 작업 필요)
    if debug is not True and service != 'payment': main_features.insert(0, "make_sheet")

    print(main_features)

    # main_features 리스트의 아이템을 차례로 실행
    for feature in main_features:
        if feature == "make_sheet":
            execute_parallel_copy("web", test_execution, service=service)

        else:
            file_path = f"{jenkins_target_directory}/web/TestCase/test_{feature}.py"
            file_name = file_path.split('/')[-1]
            # pytest 명령 실행
            try:

                subprocess.run(['pytest', file_name, '-s', '-m', marker_command],
                               cwd='/'.join(file_path.split('/')[:-1]), check=True)
                SlackWebhook().send_slack_message(f"\n\n****** {execution} - {feature} 확인완료 ******", debug=debug)

            except subprocess.CalledProcessError as e:
                print(f"[실행 오류] test_{feature}.py 파일에 실행할 {marker_command} marker가 없습니다: {e}")


def check_and_delete_binary():
    file_path = PicklePath.web_pickle_path
    try:
        os.remove(file_path)
        print("remove binary")
    except FileNotFoundError:
        pass


def main_web(test_execution="ST", debug=True, service=None, user_id=None, version=None, auto_trigger=None):
    test_execution = "RT" if debug == True else test_execution

    if service is not None: service = return_service_str(service)
    # key error 방지를 위한 데이터 생성
    check_and_delete_binary()  # 결과 파일이 있다면 초기화
    # 현재 lifestyle만 작업하기 때문에 일단 이렇게 해둡니다. 추후에 개선 필요함.
    # if (service is None and debug is None) or (service == "lifestyle" and debug is None):
    #     print(f"service : {service}")
        # base_run_names = ["Lifestyle_RT"]
        # service_names = ["lifestyle"]
        # try:
        #     run_id_dict = create_test_runs("web", test_execution, base_run_names, service_names)
        #     # for service_name in service_names:
        #     #     run_id = run_id_dict.get(service_name)
        #     #     entry_id = run_id_dict.get(service_name + "_entry")
        #     #     ResultWeb().write_result(service_name + "_run_id", run_id)
        #     #     ResultWeb().write_result(service_name + "_entry", entry_id)
        #     #     ResultWeb().write_result("web_testrail", "pass")
        #
        # except Exception as e:
        #     ResultWeb().write_result("testrail 생성 실패 :", {e})
        #     ResultWeb().write_result("web_testrail", "fail")
        #     return "테스트런 생성 실패로 실행 하지 않음."
    # else:
    #     ResultWeb().write_result("web_testrail", "none")
    if version is not None:
        from flask_active.version_func import _save_request_text_to_binary
        _save_request_text_to_binary(version,"web")

    title = "Smoke" if test_execution == "ST" else "Regression" if test_execution == "RT" else "Temporary" if test_execution == "test" else "Unknown"  # 타이틀용 string 만들기
    slack_message = f"\n\n****** Web {title} Test 시작 ******" if service is None else f"\n\n****** Web-{service} {title} Test 시작 ******"
    SlackWebhook().send_slack_message(slack_message, debug=debug)
    run_pytest(title.lower(), debug=debug, service=service, test_execution=test_execution)
    if get_terminate_value("web") == True:
        SlackWebhook().start_slack_msg("웹 자동화 테스트가 강제종료 되었습니다.")
        # delete_test_run("web")

    else:
        WebReadDictResult().execute_read_dict_result(test_execution, title, debug=debug, service=service,
                                                     user_id=user_id)

    data_payload = {
        "web_terminate": False,
        "auto_trigger":auto_trigger,
        "platform" : "web"
    }
    send_test_running_terminate_value(data_payload)

    os.remove(PicklePath.web_pickle_path)

def to_none(val: str | None) -> str | None:
    if val is None:
        return None
    if str(val).strip().lower() == 'none' or str(val).strip() == '':
        return None
    return val

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("true", "t", "1"):
        return True
    elif v.lower() in ("false", "f", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean 값은 True 또는 False로 입력해야 합니다.")

if __name__ == '__main__':
    ''' web 자동화 테스트 실행합니다
    param:
        test_execution(str) : 실행할 marker (in ["ST", "RT", "test"])
        debug(bool) : debug 사용 유무 (리포트가 디버그 채널로)
        service(str) : 하나의 서비스만 실행시킬 때 서비스 명 입력 (in ["common", "home", ""community","content","affiliate","comm_s" or "commerce_service", "comm_p" or "commerce_platform", "o2o", "search"])
    '''
    # main_web(test_execution="ST", debug=True, service=None)
    parser = argparse.ArgumentParser(description="web 자동화 테스트 실행 스크립트")
    parser.add_argument('--test_execution', default="RT", help='실행할 marker (기본: RT)')
    parser.add_argument('--debug', type=str2bool, default=True, help='디버그 사용 여부 (True 또는 False)')
    parser.add_argument('--service', type=str, default=None, help='단일 서비스명 ("common", "home","community","content","affiliate","ohsweb","CONTENTWEB","comm_s" or "commerce_service", "comm_p" or "commerce_platform", "o2o", "search")')
    parser.add_argument('--user_id', default=None, help='유저 ID (선택)')
    parser.add_argument('--version', default=None,help='수동 버전 생성용')
    parser.add_argument('--bool_trigger', default=None,help='지라 트리거 체크용')


    args = parser.parse_args()

    service = to_none(args.service)
    user_id = to_none(args.user_id)
    version = to_none(args.version)
    bool_trigger = to_none(args.bool_trigger)

    main_web(
        test_execution=args.test_execution,
        debug=args.debug,
        service=service,
        user_id=user_id,
        version=version,
        auto_trigger=bool_trigger
    )

