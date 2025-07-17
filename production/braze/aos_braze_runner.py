import os, time, subprocess, unittest, sys
from app.common.base_method.read_dict_result_braze import AosReadDictResult
from production.common.data.automation_consts import PicklePath
from production.common.data.automation_consts import BddFeaturePath
from app.common.app_config.data import UDID
import threading
from production.app.common_method.prod_STF import STFManager

device_serial = UDID.aos_prod_serial
def appium_sever_launch():
    port = 4727
    appium_server_kill_cmd = f'lsof -ti:{port} | xargs kill -9'
    os.system(appium_server_kill_cmd)
    STFManager(device_serial).remove_device()
    STFManager(device_serial).add_device()
    STFManager(device_serial).remote_connect()
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
    # result = subprocess.run(["behave", f"{BddFeaturePath.jenkins_aos_braze_path}/{feature}.feature","--no-capture"])
    feature_files = [
        f"{BddFeaturePath.jenkins_aos_braze_path}/{feature_name}.feature"
        for feature_name in main_features
    ]
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [no_capture_option]
    )
    return result.returncode


def main_braze_aos():
    os.environ["ANDROID_AUTO_FLAG"] = "0"
    try:
        os.remove(PicklePath.jenkins_prod_and_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")
    appium_sever = threading.Thread(target=appium_sever_launch)
    appium_sever.start()

    time.sleep(10)
    print("자동화 안드로이드 시작")

    main_features = ["braze_deploy", "braze_check"]

    thread_behave = threading.Thread(target=lambda: run_behave(main_features))
    thread_behave.start()

    thread_behave.join()

    AosReadDictResult().breaze_result()

    os.remove(PicklePath.jenkins_prod_and_pickle_path)

    appium_server_kill()
    appium_sever.join()


if __name__ == '__main__':
    main_braze_aos()
