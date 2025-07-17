import requests,urllib3
from urllib3.exceptions import ProtocolError

import json
from app.common.app_config.data import ApiBaseUrl
import time
from selenium.common.exceptions import TimeoutException


class ContestsCardCollectionApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_content_base_url
        self.qa_api_url = ApiBaseUrl.qa_content_base_url
    def get_scrap_count(self, product_id):
        api_url = f"{self.api_url}/api/card-collections/{product_id}"
        qa_api_url = f"{self.qa_api_url}/api/card-collections/{product_id}"

        header = {
                "Content-Type": "application/json"
                  }
        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.get(url=qa_api_url, headers=header, timeout=10)#verify=False)
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
            raise TimeoutException

        data = response.json()
        result = data['data']['scrapCount']
        return result

