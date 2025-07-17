import os, time, subprocess, unittest, sys
from production.common.data.automation_consts import BddFeaturePath,PicklePath
from app.common.app_config.data import WdaPath
from app.common.base_method.read_dict_result_braze import IosReadDictResult
from app.common.app_config.data import UDID
import threading
from app.common.base_method.ios_remote_control_func import request_wda_del


wda_1_running = False
behave_running = False

def appium_sever_launch():
    appium_sever = 'appium server -p 4723 -a 0.0.0.0 -pa /wd/hub'
    os.system(appium_sever)


def appium_server_kill():
    appium_sever_kill = 'pkill -9 -f appium '
    os.system(appium_sever_kill)
def wda_launch_1():
    global wda_1_running
    try:
        udid = UDID.iphone12mini_udid
        webdriver_agent_path = WdaPath.wda_path_1
        os.environ['USE_PORT'] = str(8100)
        process = subprocess.Popen([
            'xcodebuild',
            '-project', f"{webdriver_agent_path}/WebDriverAgent.xcodeproj",
            '-scheme', 'WebDriverAgentRunner',
            '-destination', f'id={udid}',
            '-allowProvisioningUpdates',
            'test'
        ],  stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        wda_1_running = True

        for stderr_line in iter(process.stderr.readline, ""):
            print(stderr_line, end='')
            if "TEST FAILED" in stderr_line or "BUILD INTERRUPTED" in stderr_line:
                raise Exception("WebDriverAgent test failed")

        process.stderr.close()

    except Exception as e:
        wda_1_running = False

        print(f"An error occurred in wda_launch_1: {e}")

def wda_stop():
    global wda_1_running

    try:
        pids = subprocess.check_output(["pgrep", "-f", "WebDriverAgentRunner"])
        pids = pids.strip().split(b'\n')

        for pid in pids:
            pid = pid.decode('utf-8')  # 바이트 문자열을 유니코드 문자열로 변환
            subprocess.call(["kill", pid])
            print(f"Process with PID {pid} has been terminated.")
        wda_1_running = False

    except subprocess.CalledProcessError:
        print("WebDriverAgentRunner process not found.")
def monitor_wda():
    global wda_1_running
    while behave_running:
        if not wda_1_running:
            print("wda_launch_1이 종료되었습니다! 다시 실행합니다.")
            wda_launch_start1 = threading.Thread(target=wda_launch_1)
            wda_launch_start1.start()
        time.sleep(2)

def run_behave(main_features):
    # result = subprocess.run(["behave", BddFeaturePath.jenkins_ios_braze_path,"--no-capture"])
    feature_files = [
        f"{BddFeaturePath.jenkins_ios_braze_path}/{feature_name}.feature"
        for feature_name in main_features
    ]
    no_capture_option = "--no-capture"
    result = subprocess.run(
        ["behave"] + feature_files + [no_capture_option]
    )
    return result.returncode

def main_braze_ios():
    os.environ["IOS_AUTO_FLAG"] = "0"
    global behave_running, wda_1_running
    for stop_count in range(1, 4):
        if request_wda_del(test_env="prod"):
            print(f"del complete")
            break
        else:
            print(f"del_count {stop_count} failed.")
    else:
        pass
    # for stop_count in range(1, 4):
    #     if request_wda_stop(test_env="st"):
    #         print(f"stop complete")
    #         break
    #     else:
    #         print(f"stop_count {stop_count} failed.")
    # else:
    #     pass
    #
    # for run_count in range(1, 4):
    #     if request_wda_run(test_env="st"):
    #         print(f"run complete")
    #         break
    #     else:
    #         request_wda_stop(test_env="st")
    #         print(f"run_count {run_count} failed.")
    # else:
    #     pass
    try:
        os.remove(PicklePath.jenkins_prod_ios_pickle_path)
    except FileNotFoundError:
        print("파일없음 예외처리")

    main_features = ["braze_check"]
    # Smoke = ST / Regression = RT
    print("자동화 시작")
    thread_behave = threading.Thread(target=lambda: run_behave(main_features))


    thread_behave.start()

    # behave_running = True
    # monitor_thread = threading.Thread(target=monitor_wda)
    # monitor_thread.start()

    thread_behave.join()

    IosReadDictResult().breaze_result()

    os.remove(PicklePath.jenkins_prod_ios_pickle_path)

    # request_wda_stop(test_env="st")

    # behave_running = False
    # wda_stop()
    #
    # monitor_thread.join()
    # wda_launch_start1.join()

if __name__ == '__main__':
    main_braze_ios()
