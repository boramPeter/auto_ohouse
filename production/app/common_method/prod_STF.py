import subprocess
import requests
import time, os
from selenium.common.exceptions import TimeoutException
from app.common.base_method.mysql_query import QaDataBaseManager

npm_path = "/usr/bin/npm"

os.environ["PATH"] += os.pathsep + os.path.dirname(npm_path)
# adb_command = "/usr/lib/android-sdk/platform-tools/adb"
adb_command = "adb"

class STFManager:
    MAX_RETRIES = 3
    RETRY_INTERVAL = 1
    def __init__(self,DEVICE_SERIAL):
        self.STF_URL = ""
        self.STF_TOKEN = ""
        self.DEVICE_SERIAL = DEVICE_SERIAL

    def _send_request(self, method, url, func_name, headers=None, data=None):
        retries = 0
        while retries < self.MAX_RETRIES:
            response = requests.request(method, url, headers=headers, json=data)
            if response.status_code == 200:
                return response.json()
            retries += 1
            time.sleep(self.RETRY_INTERVAL)
        raise TimeoutException(f"{func_name} 실행시에 {url}로 보내는 데 {self.MAX_RETRIES}번 재시도하였으나 실패함.응답 코드: {response.status_code}")

    def add_device(self):
        data = {"serial": self.DEVICE_SERIAL}
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.STF_TOKEN}
        response = self._send_request("POST", f"{self.STF_URL}/api/v1/user/devices", "add_device", headers=headers, data=data)
        print(response)
        return response

    def remote_connect(self):
        headers = {"Authorization": "Bearer " + self.STF_TOKEN}
        response = self._send_request("POST", f"{self.STF_URL}/api/v1/user/devices/{self.DEVICE_SERIAL}/remoteConnect","remote_connect",headers=headers)
        success = response.get("success")
        description = response.get("description")

        if not success:
            print(f"리모트 실패 이유: {description}")
            return

        remote_connect_url = response.get("remoteConnectUrl")
        QaDataBaseManager().insert_or_update_device_info(self.DEVICE_SERIAL, remote_connect_url)
        subprocess.run([adb_command, "connect", remote_connect_url])
        return remote_connect_url

    def remove_device(self):
        headers = {"Authorization": "Bearer " + self.STF_TOKEN}
        response = requests.request("DELETE", f"{self.STF_URL}/api/v1/user/devices/{self.DEVICE_SERIAL}", headers=headers)
        print(response)
        return response

    def put_adb_key(self, ):
        file_path = os.path.expanduser('~/.android/adbkey.pub')
        result = subprocess.run(['cat', file_path], capture_output=True, text=True, check=True)

        headers = {
            "Authorization": "Bearer " + self.STF_TOKEN,
            "Content-Type": "application/json"  # JSON 형식으로 요청을 보냄
        }
        data = {
            "publickey": result.stdout.strip()

        }
        response = requests.post(f"{self.STF_URL}/api/v1/user/adbPublicKeys", headers=headers, json=data)

        print(f"put_adb_key text: {response.text}")  # 응답 본문 출력
        return response

    def get_device_remote_connect_url(self):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.STF_TOKEN}
        response = self._send_request("GET", f"{self.STF_URL}/api/v1/user/devices", "get_device_remote_connect_url",headers=headers)
        devices = response.get("devices", [])
        for device in devices:
            if device.get("serial") == self.DEVICE_SERIAL:
                return device.get("remoteConnectUrl")
        return None

'''
1. 테스트 시작 전에 stf api를 호출한다
2. data에 있는 시리얼넘버로 api를 호출해서 디바이스별 remoteConnectUrl를 디비에 적재한다. -> remote api
3. data에는 시리얼넘버와, remoteConnectUrl을 호출하게끔 함수로 만들어야 한다. -> 클래스변수로 만들어야 코드수정이 없음. db조회로 변경
4. 안드로이드만 테스트 시작 전에, 프리컨디션 0번을 만들고 stf연결하는 사전조건을 추가해야한다. -> hook
5. 만약 연결 실패했다면, (3트) 테스트를 강제종료 시켜야 한다.
'''
