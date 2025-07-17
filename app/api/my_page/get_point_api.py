import time
import requests, urllib3
import json
from datetime import datetime
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError
from app.common.app_config.data import AppVersion
from app.common.base_method.ios_result_binary import Result

class PointAPI:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    #
    def get_point(self, user_id, cookie_value, token):

        qa_api_url = f""

        header = {
                "Content-Type": "application/json",
                "ohouse-os-type":"iOS",
                "ohouse-user-id": f"{user_id}",
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "authorization": f"Bearer {token}"
                  }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = requests.get(url=qa_api_url, headers=header, timeout=10)#verify=False)
                result = response.json()['mileage']
                if response.status_code == 200:
                    return result
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
            print("재시도횟수 많아서 예외처리")
            raise TimeoutException
