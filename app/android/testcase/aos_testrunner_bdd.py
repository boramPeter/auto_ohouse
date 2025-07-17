import os, time, subprocess, unittest, sys
from app.common.base_method.read_dict_result import AosReadDictResult
from app.common.app_config.data import PicklePath
from app.common.app_config.data import BddFeaturePath
from app.common.base_method.aos_result_binary import ResultAndroid
import concurrent.futures
from report.create_report import AppCreateSlackReport
from app.common.app_config.data import UDID
import threading
from production.app.common_method.prod_STF import STFManager
from report.goole_spread_sheet_func.make_spread_sheet_func import execute_parallel_copy
# from report.testrail_func.festrail_api import create_test_runs,delete_test_run
from report.slack_webhook import SlackWebhook
from flask_active.test_running_check.running_value_provider import get_terminate_value,send_test_running_terminate_value
import argparse

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


device_serial1 = UDID.galaxy_serial_1
device_serial2 = UDID.galaxy_serial_2
device_serial3 = UDID.galaxy_serial_rt

'''
4725 : st1
4726 : st2
4727 : prod
4728 : rt
'''
def appium_sever_launch1():
    STFManager(device_serial1).remove_device()
    STFManager(device_serial1).add_device()
    STFManager(device_serial1).remote_connect()

    npm_path = "/usr/local/bin/npm"
    os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)

    appium_command = [
        "/usr/local/bin/appium",
        f"--default-capabilities",
        f'{{"udid":"{UDID.galaxy_udid_1}"}}',
        "-p", "4725",
        "-a", "0.0.0.0",
        "-pa", "/wd/hub"
    ]

    print("appium_sever_launch1 appium_commands start")
    subprocess.run(appium_command)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("appium_sever_launch1 appium_commands complete")

def appium_sever_launch2():
    STFManager(device_serial2).remove_device()
    STFManager(device_serial2).add_device()
    STFManager(device_serial2).remote_connect()

    npm_path = "/usr/local/bin/npm"
    os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)

    appium_command = [
        "/usr/local/bin/appium",
        f"--default-capabilities",
        f'{{"udid":"{UDID.galaxy_udid_2}"}}',
        "-p", "4726",
        "-a", "0.0.0.0",
        "-pa", "/wd/hub"
    ]

    print("appium_sever_launch2 appium_commands start")
    subprocess.run(appium_command)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("appium_sever_launch2 appium_commands complete")

def appium_sever_launch3():
    STFManager(device_serial3).remove_device()
    STFManager(device_serial3).add_device()
    STFManager(device_serial3).remote_connect()

    npm_path = "/usr/local/bin/npm"
    os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)

    appium_command = [
        "/usr/local/bin/appium",
        f"--default-capabilities",
        f'{{"udid":"{UDID.galaxy_udid_rt}"}}',
        "-p", "4728",
        "-a", "0.0.0.0",
        "-pa", "/wd/hub"
    ]

    print("appium_sever_launch3 appium_commands start")
    subprocess.run(appium_command)#, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("appium_sever_launch3 appium_commands complete")

def launch_appium_servers():
    ports = [4725, 4726, 4728]
    for port in ports:
        appium_server_kill_cmd = f'/usr/sbin/lsof -ti:{port} | xargs kill -9'
        os.system(appium_server_kill_cmd)

    STFManager(device_serial1).remove_device()
    STFManager(device_serial1).add_device()
    STFManager(device_serial1).remote_connect()
    STFManager(device_serial1).put_adb_key()


    STFManager(device_serial2).remove_device()
    STFManager(device_serial2).add_device()
    STFManager(device_serial2).remote_connect()
    STFManager(device_serial2).put_adb_key()

    STFManager(device_serial3).remove_device()
    STFManager(device_serial3).add_device()
    STFManager(device_serial3).remote_connect()
    STFManager(device_serial3).put_adb_key()

    os.environ['ANDROID_HOME'] = '/usr/lib/android-sdk'
    npm_path = "/usr/bin/npm"
    os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)
    appium_path = os.popen("which appium").read().strip()
    appium_commands = [
        [appium_path, f"--default-capabilities", f'{{"udid":"{UDID.galaxy_udid_1}"}}', "-p", "4725", "-a", "0.0.0.0", "-pa", "/wd/hub"],
        [appium_path, f"--default-capabilities", f'{{"udid":"{UDID.galaxy_udid_2}"}}', "-p", "4726", "-a", "0.0.0.0", "-pa", "/wd/hub"],
        [appium_path, f"--default-capabilities", f'{{"udid":"{UDID.galaxy_udid_rt}"}}', "-p", "4728", "-a", "0.0.0.0","-pa", "/wd/hub"]

    ]

    print("Launching Appium servers...")
    for command in appium_commands:
        subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Appium servers launched successfully")


def appium_server_kill():
    ports = [4725, 4726, 4728]
    for port in ports:
        appium_server_kill_cmd = f'/usr/sbin/lsof -ti:{port} | xargs kill -9'
        os.system(appium_server_kill_cmd)

    STFManager(device_serial1).remove_device()
    STFManager(device_serial2).remove_device()
    STFManager(device_serial3).remove_device()


def run_behave(main_features, tags):

    # try:
    #     if ResultAndroid().read_result_slack("is_aos_running") == "false":
    #         return
    # except FileNotFoundError:
    #     return
    # except KeyError:
    #     return
    # if feature == "count_run_rate":
    #     count_run_case(test_execution, debug=debug)
    #     return
    # else:
    #     result = subprocess.run(
    #         ["behave", f"{BddFeaturePath.aos_bdd_path}/{feature}.feature", f"--tags={tags}","--no-capture"])
    #     return result.returncode
    feature_files = [
        f"{BddFeaturePath.aos_bdd_path}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags={tags}"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )
    return result.returncode


def run_behave2(main_features, test_execution,tags, debug=None):
    # ResultAndroid().write_result("android_testrail", "None")
    # base_run_names = ["Lifestyle_RT", "Ads_RT"]
    # service_names = ["lifestyle", "ads"]
    if debug is not True:
        execute_parallel_copy("aOS",test_execution)

        """
        - poc 이후 적용시에 서비스 추가 필요
        - 프리컨디션, 환경설정파일, 익셉션핸들러에 영향있음. 
        """

        # try :
        #     run_id_dict = create_test_runs("aOS",test_execution, base_run_names, service_names)
        #     for service in service_names:
        #         run_id = run_id_dict.get(service)
        #         entry_id = run_id_dict.get(service+"_entry")
        #         ResultAndroid().write_result(service+"_run_id", run_id)
        #         ResultAndroid().write_result(service+"_entry", entry_id)
        #         ResultAndroid().write_result("android_testrail", "pass")
        #
        # except Exception as e:
        #     print(f"testrail 생성 실패 : {e}")
        #     ResultAndroid().write_result("android_testrail", "fail")
        #     return "테스트런 생성 실패로 실행 하지 않음."
    # else:
    #     for service in service_names:
    #         ResultAndroid().write_result(service + "_run_id", "None")
    #         ResultAndroid().write_result(service + "_entry", "None")
    #         ResultAndroid().write_result("android_testrail", "pass")

    feature_files = [
        f"{BddFeaturePath.aos_bdd_path2}/{feature_name}.feature"
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
        f"{BddFeaturePath.aos_bdd_path3}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags={tags}"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )
    return result.returncode

def count_run_case(test_execution, debug=None):
    return AppCreateSlackReport().is_run_rate("Android", test_execution, debug=debug,idx=None)

def main_aos(test_execution,debug=None,service=None,user_id=None,platform="aOS",version=None):
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    # os.chdir(current_dir)
    # test_execution = "RT" if debug == True else test_execution
    os.environ["ANDROID_AUTO_FLAG"] = "0"

    print(f"main_aos debug : {debug}")
    # Smoke = ST / Regression = RT
    if test_execution == "ST":
        tags = "@PRE,@ST"
        test_run = "ST"
    elif test_execution == "RT":
        tags = "@PRE,@ST,@RT"
        test_run = "RT"
    else:
        tags = "@PRE,@ST"
        test_run = "ST"

    appium_sever = threading.Thread(target=launch_appium_servers)
    appium_sever.start()
    print("start")

    if service is None:
        # main_features = ["pre_condition"]
        main_features = ["pre_condition", "common","comm_service", "home","community","content","affiliate","search", "o2o","ads", "comm_platform","payment","mkt"]
        # main_features = ["pre_condition", "common","comm_service","life_style","comm_platform"]

    else:
        tags = "@PRE,@ST,@개별" if test_run == "ST" else "@PRE,@ST,@RT,@개별"
        main_features =["pre_condition",service]

    #main_features = ["pre_condition", "common", "count_run_rate", "comm_service", "count_run_rate", "comm_platform", "search", "o2o", "count_run_rate", "ads", "mkt"]
    try:
        os.remove(PicklePath.aos_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")

    if debug:
        tags += ",@True"
    if version is not None:
        from flask_active.version_func import _save_request_text_to_binary
        _save_request_text_to_binary(version,platform)
    time.sleep(0.5)
    ResultAndroid().write_result("test_execution_debug", "True") if debug is not True else ResultAndroid().write_result("test_execution_debug", "False")
    time.sleep(0.5)
    ResultAndroid().write_result("is_aos_running", "true")
    time.sleep(0.5)
    # ResultAndroid().write_result("android_testrail", "None")
    # time.sleep(0.5)
    ResultAndroid().write_result("test_execution", tags)
    time.sleep(0.5)

    try:
        udid_1 = STFManager(device_serial1).remote_connect()
        os.environ["UDID_1"] = udid_1

        udid_2 = STFManager(device_serial2).remote_connect()
        os.environ["UDID_2"] = udid_2

        udid_3 = STFManager(device_serial3).remote_connect()
        os.environ["UDID_3"] = udid_3

    except Exception as e:
        SlackWebhook().start_slack_msg(f"STF 연결에 실패하였습니다. {e}")
        data_payload = {
            "android_terminate": True
        }
        send_test_running_terminate_value(data_payload)

    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            future_behave = executor.submit(
                lambda: [run_behave(main_features, tags)])
            future_behave2 = executor.submit(
                lambda: [run_behave2(main_features, test_run, tags, debug=debug)])
            future_behave3 = executor.submit(
                lambda: [run_behave3(main_features, tags)])

            futures.extend([future_behave, future_behave2, future_behave3])

            for future in concurrent.futures.as_completed(futures):
                pass  # 결과 활용 예정
    if ResultAndroid().read_result_slack(
        "is_aos_running") == "false":
        SlackWebhook().start_slack_msg(f"안드로이드 자동화 테스트가 중단되었습니다. 테스트 수행 로그를 확인해주세요")
    elif debug is not True and ResultAndroid().read_result_slack("android_spreadsheet") == "":
        SlackWebhook().start_slack_msg(f"스프레드시트 생성에 실패하여 테스트 강제종료.")
    # elif debug is not True and ResultAndroid().read_result_slack("android_testrail") == "fail":
    #     SlackWebhook().start_slack_msg(f"테스트레일 run 생성에 실패하여 테스트 강제종료.")
    elif get_terminate_value("android") == True:
        SlackWebhook().start_slack_msg("안드로이드 자동화 테스트가 강제종료 되었습니다.")
        # delete_test_run("aOS")
    else:
        print(f"리포팅 전 플래그 체크 {test_execution,debug,service}")

        AosReadDictResult().execute_read_dict_result(test_execution,debug=debug,individual=service,user_id=user_id)

    # 강종 플래그 업데이트
    data_payload = {
        "android_terminate": False
    }
    send_test_running_terminate_value(data_payload)
    os.remove(PicklePath.aos_pickle_path)

    appium_server_kill()
    appium_sever.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_execution', default="RT", help='실행 모드 (기본: RT)')
    parser.add_argument('--debug', type=str2bool, default=True, help='디버그 모드 (True 또는 False)')
    parser.add_argument('--service', type=str, default=None, help='서비스 이름 ("pre_condition", "common","comm_service", "home","community","content","affiliate","search", "o2o","ads", "comm_platform","payment","mkt")')
    parser.add_argument('--user_id', default=None,help='유저 ID (선택)')
    parser.add_argument('--version', default=None,help='수동 버전 생성용')

    args = parser.parse_args()

    service = to_none(args.service)
    user_id = to_none(args.user_id)
    version = to_none(args.version)

    main_aos(
        test_execution=args.test_execution,
        debug=args.debug,
        service=service,
        user_id=user_id,
        version=version
    )
