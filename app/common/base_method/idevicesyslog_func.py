import subprocess,os
import threading
import time
import re
from app.common.app_config.data import UDID

from selenium.common.exceptions import TimeoutException
import concurrent.futures


class MediaPlayingChecker:
    def check_log_existence(self, udid,timeout=20):
        start_time = time.time()
        elapsed_time = 0  # 변수 초기화
        shell_command = os.popen("which idevicesyslog").read().strip() or "/opt/homebrew/bin/idevicesyslog"
        command = f"{shell_command} -u {udid}"
        grep_pattern = "mAudioToolboxIsPlaying = PLAYING"

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        while True:
            output_line = process.stdout.readline()
            if not output_line and process.poll() is not None:
                break

            if re.search(grep_pattern, output_line):
                print("결과 확인됨")
                process.terminate()
                break

            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                print("시간 초과. 결과가 없음.")
                process.terminate()
                break

        process.wait()
        return True if elapsed_time <= timeout else False


class SoundCheckProvider:
    executor = concurrent.futures.ThreadPoolExecutor()
    def actual_result(self, device_udid):
        self.executor = SoundCheckProvider.executor
        futures = []
        future = self.executor.submit(MediaPlayingChecker().check_log_existence, device_udid, 20)
        futures.append(future)
        # 결과 확인 및 처리


        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                return True
            else:
                return False