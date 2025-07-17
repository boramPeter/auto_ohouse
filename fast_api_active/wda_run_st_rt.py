import os, time, subprocess
from app.common.app_config.data import WdaPath
from app.common.app_config.data import UDID
import threading
from datetime import datetime

wda_1_running = False
wda_2_running = False
wda_3_running = False
behave_running = False

def wda_launch_1():
    global wda_1_running
    try:
        wda_1_running = True

        udid = UDID.iphone12mini_udid
        webdriver_agent_path = WdaPath.wda_path_1
        os.environ['USE_PORT'] = str(8100)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H")
        log_file_path = f""
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

            process.stdout.close()
            process.stderr.close()

    except Exception as e:
        wda_1_running = False
        print(f"An error occurred in wda_launch_1: {e}")

def wda_launch_2():
    global wda_2_running
    try:
        wda_2_running = True
        udid = UDID.iphone11_udid
        webdriver_agent_path = WdaPath.wda_path_2
        os.environ['USE_PORT'] = str(8101)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H")
        log_file_path = f""
        with open(log_file_path, "w") as log_file2:
            process = subprocess.Popen([
                'xcodebuild',
                '-project', f"{webdriver_agent_path}/WebDriverAgent.xcodeproj",
                '-scheme', 'WebDriverAgentRunner',
                '-destination', f'id={udid}',
                '-allowProvisioningUpdates',
                'test'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            for stdout_line in iter(process.stdout.readline, ""):
                log_file2.write(stdout_line)

            for stderr_line in iter(process.stderr.readline, ""):
                print(stderr_line, end='')
                log_file2.write(stderr_line)
                if "TEST FAILED" in stderr_line or "BUILD INTERRUPTED" in stderr_line:
                    raise Exception("WebDriverAgent test failed")

    except Exception as e:
        wda_2_running = False
        print(f"An error occurred in wda_launch_2: {e}")

def wda_launch_3():
    global wda_3_running
    try:
        wda_3_running = True
        udid = UDID.iphone_rt_udid
        webdriver_agent_path = WdaPath.wda_path_3
        os.environ['USE_PORT'] = str(8103)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H")
        log_file_path = f""
        with open(log_file_path, "w") as log_file3:
            process = subprocess.Popen([
                'xcodebuild',
                '-project', f"{webdriver_agent_path}/WebDriverAgent.xcodeproj",
                '-scheme', 'WebDriverAgentRunner',
                '-destination', f'id={udid}',
                '-allowProvisioningUpdates',
                'test'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            for stdout_line in iter(process.stdout.readline, ""):
                log_file3.write(stdout_line)

            for stderr_line in iter(process.stderr.readline, ""):
                print(stderr_line, end='')
                log_file3.write(stderr_line)
                if "TEST FAILED" in stderr_line or "BUILD INTERRUPTED" in stderr_line:
                    raise Exception("WebDriverAgent test failed")

    except Exception as e:
        wda_3_running = False
        print(f"An error occurred in wda_launch_3: {e}")

def wda_st_rt_stop(udid1=None,udid2=None,udid3=None):
    global wda_1_running,wda_2_running,wda_3_running

    try:
        if udid1 is not None:
            command = f'ps aux | grep "xcodebuild" | grep "{udid1}" | grep -v "grep" | awk \'{{print $2}}\' | xargs kill'
            subprocess.run(command, shell=True, check=True)
            print("1번 프로세스 종료 성공")
            wda_1_running = False
        if udid2 is not None:
            command = f'ps aux | grep "xcodebuild" | grep "{udid2}" | grep -v "grep" | awk \'{{print $2}}\' | xargs kill'
            subprocess.run(command, shell=True, check=True)
            print("2번 프로세스 종료 성공")
            wda_2_running = False

        if udid3 is not None:
            command = f'ps aux | grep "xcodebuild" | grep "{udid3}" | grep -v "grep" | awk \'{{print $2}}\' | xargs kill'
            subprocess.run(command, shell=True, check=True)
            print("3번 프로세스 종료 성공")
            wda_3_running = False

    except subprocess.CalledProcessError:
        print("WebDriverAgentRunner process not found.")

def monitor_wda():
    global wda_1_running, wda_2_running, wda_3_running
    timestamp = datetime.now().strftime("%Y-%m-%d_%H")
    def _log_message(name,message):
        log_file_path = f"/Users/qa_auto1/Desktop/data/wda_log_3/{name}_{timestamp}.txt"
        with open(log_file_path, 'a') as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    while wda_1_running and wda_2_running and wda_3_running:
        if not wda_1_running:
            print(f"wda_1_running set value:{wda_1_running}")
            wda_st_rt_stop(udid1=UDID.iphone12mini_udid)
            _log_message("wda_1_running","wda_launch_1 종료되었습니다! 다시 실행합니다.")
            wda_launch_start1 = threading.Thread(target=wda_launch_1)
            wda_launch_start1.start()
        if not wda_2_running:
            print(f"wda_2_running set value:{wda_2_running}")
            wda_st_rt_stop(udid2=UDID.iphone11_udid)
            _log_message("wda_2_running","wda_launch_2 종료되었습니다! 다시 실행합니다.")
            wda_launch_start2 = threading.Thread(target=wda_launch_2)
            wda_launch_start2.start()

        if not wda_3_running:
            print(f"wda_3_running set value:{wda_3_running}")
            wda_st_rt_stop(udid2=UDID.iphone_rt_udid)
            _log_message("wda_3_running","wda_launch_3 종료되었습니다! 다시 실행합니다.")
            wda_launch_start3 = threading.Thread(target=wda_launch_3)
            wda_launch_start3.start()
        time.sleep(2)

def run_st_rt_wda():
    global wda_1_running, wda_2_running, wda_3_running

    wda_st_rt_stop(udid1=UDID.iphone12mini_udid,udid2=UDID.iphone11_udid,udid3=UDID.iphone_rt_udid)

    wda_launch_start1 = threading.Thread(target=wda_launch_1)
    wda_launch_start1.start()

    wda_launch_start2 = threading.Thread(target=wda_launch_2)
    wda_launch_start2.start()

    wda_launch_start3 = threading.Thread(target=wda_launch_3)
    wda_launch_start3.start()

    timeout = 100  # 최대 대기 시간 (초)
    elapsed_time = 0  # 경과 시간 초기화

    while not (wda_1_running and wda_2_running and wda_3_running) and elapsed_time < timeout:
        print("wda_launch 함수가 실행 중이 아닙니다. 1초 대기 후 다시 확인합니다.")
        time.sleep(0.5)
        elapsed_time += 1
        if elapsed_time >= timeout:
            print("최대 대기 시간을 초과했습니다.")


    monitor_thread = threading.Thread(target=monitor_wda)
    monitor_thread.start()

    def background_task():
        monitor_thread.join()
        time.sleep(1)
        wda_launch_start1.join()
        time.sleep(1)
        wda_launch_start2.join()
        time.sleep(1)
        wda_launch_start3.join()

    return background_task
