import os, time, subprocess, unittest, sys
from production.common.method.result_binary import TestResult
from production.common.data.automation_consts import PicklePath
from production.common.data.automation_consts import BddFeaturePath

from app.common.app_config.data import UDID
import threading
from production.app.common_method.prod_STF import STFManager
from production.common.method.log_to_slack_func import ReadDictResult

device_serial = UDID.aos_prod_serial


def appium_sever_launch():
    port = 4727
    # appium_server_kill_cmd = f'/usr/sbin/lsof -ti:{port} | xargs kill -9'
    # os.system(appium_server_kill_cmd)
    STFManager(device_serial).remove_device()
    STFManager(device_serial).add_device()
    STFManager(device_serial).remote_connect()
    # adb키 추가
    STFManager(device_serial).put_adb_key()

    npm_path = "/usr/bin/npm"
    os.environ['ANDROID_HOME'] = '/usr/lib/android-sdk'
    os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)
    appium_path = os.popen("which appium").read().strip()
    appium_server_command = [appium_path, f"--default-capabilities", f'{{"udid":"{UDID.aos_prod_udid}"}}',
                             "-p", "4727", "-a", "0.0.0.0", "-pa", "/wd/hub"]

    print("Launching Appium servers...")
    subprocess.Popen(appium_server_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Appium servers launched successfully")

def appium_server_kill():
    port = 4727
    appium_server_kill_cmd = f'lsof -ti:{port} | xargs kill -9'
    os.system(appium_server_kill_cmd)
    STFManager(device_serial).remove_device()


def run_behave(main_features):
    # result = subprocess.run(
    #     ["behave", f"{BddFeaturePath.prod_aos_bdd_path}/{feature}.feature",'--tags=@PRE,@Prod',"--no-capture"])
    # return result.returncode
    feature_files = [
        f"{BddFeaturePath.jenkins_prod_aos_bdd_path}/{feature_name}.feature"
        for feature_name in main_features
    ]
    tags_option = f"--tags=@PRE,@Prod"
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [tags_option, no_capture_option]
    )
    return result.returncode

def main_aos_prod():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)
    os.environ["ANDROID_AUTO_FLAG"] = "0"
    appium_sever = threading.Thread(target=lambda: appium_sever_launch())
    appium_sever.start()

    main_features = ["pre_condition","common","home","commerce_service","my_page","lifestyle","search","o2o","commerce_platform"]
    # main_features = ["pre_condition"]

    try:
        os.remove(PicklePath.jenkins_prod_and_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")
        
    udid_prod = STFManager(device_serial).remote_connect()
    os.environ["PROD_REMOTE_URL"] = udid_prod
    print(f'PROD_REMOTE_URL 설정: {os.environ.get("PROD_REMOTE_URL")}')
    
    thread_behave = threading.Thread(target=lambda: run_behave(main_features))
    thread_behave.start()


    thread_behave.join()

    appium_server_kill()
    appium_sever.join()

    ReadDictResult().send_result_slack()
    TestResult().insert_results_from_binary_to_db(platform="android")
    os.remove(PicklePath.jenkins_prod_and_pickle_path)


if __name__ == '__main__':
    main_aos_prod()
