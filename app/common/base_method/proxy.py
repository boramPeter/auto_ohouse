import subprocess
import uuid, re
import threading, time
from app.common.base_method.ios_result_binary import Result
from selenium.common.exceptions import TimeoutException

class SetMitmproxy:
    def __init__(self):
        self.process = None

    def get_locol_ip(self):
        cmd = '/usr/sbin/ipconfig getifaddr en0'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        wifi_ip = str(output.decode().strip())
        return wifi_ip

    def make_idfv(self):
        random_idfv = uuid.uuid4()
        print(f"{random_idfv}생성 완료")
        return str(random_idfv).upper()

    def get_idfv(self):
        try:
            uuid = Result().read_result_slack("uuid")
        except KeyError:
            self.put_idfv()
            uuid = Result().read_result_slack("uuid")
        return uuid

    def put_idfv(self):
        uuid = self.make_idfv()
        Result().write_result("uuid", uuid)
        print(f"{uuid}추가 완료")

    def set_mitmproxy(self, script_path):


        listenHost = SetMitmproxy().get_locol_ip()
        listenPort = 8888
        print(listenHost)
        proxy_on_command = "/usr/sbin/networksetup -setwebproxy 'Wi-Fi' localhost 8888 && /usr/sbin/networksetup -setsecurewebproxy 'Wi-Fi' localhost 8888"
        command = [
            'mitmdump',
            '--set', 'ignore_hosts="^(?!.*api\\.qa\\.dailyhou\\.se/ads/gateway/).*"',
            '-s', f"../../common/mitm_scripts/{script_path}.py",
            '-p', str(listenPort),
            #'-w', f'+{listenHost}',
        ]
        print(f"command: {command}")
        proxy_off = "/usr/sbin/networksetup -setwebproxystate 'Wi-Fi' off && /usr/sbin/networksetup -setsecurewebproxystate 'Wi-Fi' off"
        max_retries = 4
        retry_count = 0
        success = False
        self.process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("mitmdump 실행중")

        while not success and retry_count < max_retries:
            try:
                subprocess.run(proxy_on_command, shell=True, check=True, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                output = subprocess.run("networksetup -getwebproxy 'Wi-Fi'", shell=True, capture_output=True, text=True)
                if "Enabled: No" in output.stdout:
                    print("프록시가 활성화되지 않았습니다. 재시도합니다.")
                    raise subprocess.CalledProcessError(returncode=1, cmd=proxy_on_command)

                print("포트 오픈 완료")
                self.process.wait()
                success = True
            except subprocess.CalledProcessError as e:
                retry_count += 1
                print("재시도 중...")
                subprocess.run(proxy_off, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(1)
        if not success:
            print("재시도 횟수를 초과하여 예외를 발생시킵니다.")
            raise TimeoutException
    def init_mitmproxy(self):
        if self.process is not None:  # self.process가 None이 아닌 경우에만 실행
            self.process.terminate()
            print("프로세스종료완료")
        else:
            print("실행된 프로세스가 없습니다.")
        proxy_off_command = "/usr/sbin/networksetup -setwebproxystate 'Wi-Fi' off && /usr/sbin/networksetup -setsecurewebproxystate 'Wi-Fi' off"
        subprocess.run(proxy_off_command, shell=True, check=True)
        print("포트 종료완료")

    def run_mitmproxy(self, script_path):
        self.thread = threading.Thread(target=self.set_mitmproxy, args=(script_path,))
        self.thread.start()

global_mitmproxy_instance = SetMitmproxy()
