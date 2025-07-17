import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
import time
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class AddressApi:
    def is_address_input_api(self, cookie_value):
        qa_base_url = ApiBaseUrl.qa_o2o_url
        prd_base_url = ApiBaseUrl.prd_o2o_url

        api_url = f"{prd_base_url}/api/address/recent"
        qa_api_url = f"{qa_base_url}/api/address/recent"

        payload = {
                      "addressId": "",
                      "address": "서울특별시 송파구 올림픽로 135 (잠실동, 리센츠)",
                      "type": 2
                    }

        header = {
            "Content-Type": "application/json",
            'Cookie': f'_ohouse_session_4={cookie_value}'
        }

        max_retries = 5  # 최대 재시도 횟수
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header,timeout=10, data=json.dumps(payload))#verify=False)
                if response.status_code == 200:
                    break
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
            raise TimeoutException ("input api 에서 200 안내려옴")

