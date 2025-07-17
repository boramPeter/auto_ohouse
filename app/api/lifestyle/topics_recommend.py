import requests, urllib3
import json
import re
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from requests.exceptions import JSONDecodeError
from app.common.app_config.data import AppVersion
from urllib3.exceptions import ProtocolError

class TopicsRecommend:
    def count_recommend_keywords(self, test_os, version):
        prd_base_url = ApiBaseUrl.prd_base_url
        api_url = f"{prd_base_url}/content/feed/topics/recommend?app=true&os_type={test_os}&v=2&version={version}"

        qa_base_url = ApiBaseUrl.qa_base_url
        qa_api_url = f"{qa_base_url}/content/feed/topics/recommend?app=true&os_type={test_os}&v=2&version={version}"

        header = {"Content-Type": "application/json"}
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
        names = []
        idx = 0
        while True:
            try:
                keyword = response.json()['filter']['keywords'][idx]['name']
                names.append(keyword)
                idx += 1
            except IndexError:
                break

        print(names)
        return names


