import os, time, subprocess
from app.common.app_config.data import WdaPath
from app.common.app_config.data import UDID
import threading
from datetime import datetime

wda_prod_running = False

def prod_wda_launch():
    global wda_prod_running
    try:
        wda_prod_running = True
        udid = UDID.iphone_13_mini_udid
        webdriver_agent_path = WdaPath.wda_path_prod
        os.environ['USE_PORT'] = str(8102)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H")
        log_file_path = f"/Users/qa_auto1/Desktop/data/wda_log_prod/wda_log_prod{timestamp}.txt"
        with open(log_file_path, "w") as log_file:
            process = subprocess.Popen([
                'xcodebuild',
                '-project', f"{webdriver_agent_path}/WebDriverAgent.xcodeproj",
                '-scheme', 'WebDriverAgentRunner',
                '-destination', f'id={udid}',
                '-allowProvisioningUpdates',
                'test'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)


            for stdout_line in iter(process.stdout.readline, ""):
                log_file.write(stdout_line)

            for stderr_line in iter(process.stderr.readline, ""):
                print(stderr_line, end='')
                log_file.write(stderr_line)
                if "TEST FAILED" in stderr_line or "BUILD INTERRUPTED" in stderr_line:
                    raise Exception("WebDriverAgent test failed")
            time.sleep(2)
            process.stdout.close()
            process.stderr.close()

    except Exception as e:
        wda_prod_running = False
        print(f"An error occurred in wda_prod_running: {e}")

def wda_prod_stop(udid_prod=None):
    global wda_prod_running
    try:
        if udid_prod is not None:
            command = f'ps aux | grep "xcodebuild" | grep "{udid_prod}" | grep -v "grep" | awk \'{{print $2}}\' | xargs kill'
            subprocess.run(command, shell=True, check=True)
            print("프로세스 종료 성공")
            wda_prod_running = False

    except subprocess.CalledProcessError:
        print("WebDriverAgentRunner process not found.")

def monitor_wda():
    global wda_prod_running
    timestamp = datetime.now().strftime("%Y-%m-%d_%H")
    def _log_message(name,message):
        log_file_path = f"/Users/qa_auto1/Desktop/data/wda_log_prod/{name}_{timestamp}.txt"
        with open(log_file_path, 'a') as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    while wda_prod_running:
        if not wda_prod_running:
            print(f"wda_prod_running set value:{wda_prod_running}")
            wda_prod_stop(udid_prod=UDID.iphone_13_mini_udid)
            _log_message("wda_1_running","wda_prod_running 종료되었습니다! 다시 실행합니다.")
            wda_prod_running = threading.Thread(target=prod_wda_launch)
            wda_prod_running.start()
        time.sleep(2)

def run_prod_wda():
    global wda_prod_running

    wda_prod_stop(udid_prod= UDID.iphone_13_mini_udid)

    prod_wda_launch_thread = threading.Thread(target=prod_wda_launch)
    prod_wda_launch_thread.start()

    time.sleep(20)

    timeout = 100  # 최대 대기 시간 (초)
    elapsed_time = 0  # 경과 시간 초기화

    while not wda_prod_running and elapsed_time < timeout:
        print("prod_wda_launch 함수가 실행 중이 아닙니다. 1초 대기 후 다시 확인합니다.")
        time.sleep(1)
        elapsed_time += 1
        if elapsed_time >= timeout:
            print("최대 대기 시간을 초과했습니다.")

    monitor_thread = threading.Thread(target=monitor_wda)
    monitor_thread.start()

    def background_task():
        monitor_thread.join()
        time.sleep(1)
        prod_wda_launch_thread.join()
    return background_task



