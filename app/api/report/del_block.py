import requests,urllib3
import json
from app.common.app_config.data import ApiBaseUrl
import time
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class BlockDeleteClass:

    def del_block(self, user_id):
        api_url = ""

        header = {
                "Content-Type": "application/json"
                  }

        payload = {
                      "userId": user_id
                    }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = requests.post(url=api_url, headers=header, timeout=10,data=json.dumps(payload))#verify=False)
                if response.status_code == 200:
                    return response.status_code
                else:
                    retry_count += 1
                    time.sleep(1)
            except requests.exceptions.ProxyError as e:
                print(f"ProxyError 발생: {e}")
                retry_count += 1
                time.sleep(1)
            except urllib3.exceptions.ProxyError as e:
                print(f"urllib3 ProxyError 발생: {e}")
                retry_count += 1
                time.sleep(1)
            except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                print(f"ConnectionError,ProtocolError 발생: {e}")
                retry_count += 1
                time.sleep(1)
        if retry_count == max_retries:
            print("유저아이디 확인필요")
            raise TimeoutException("유저아이디 확인필요")




