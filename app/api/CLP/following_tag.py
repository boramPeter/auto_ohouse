import time
import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class ProviderFollowingTag:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def follow_hash_tag(self, tag_name, test_os, version, user_id, cookie_value, token):
        api_url = f"{self.api_url}/content/following-hashtags/{tag_name}?app=true&os_type={test_os}&v=2&version={version}"
        qa_api_url = f"{self.qa_api_url}/content/following-hashtags/{tag_name}?app=true&os_type={test_os}&v=2&version={version}"

        header = {
                "Content-Type": "application/json",
                "ohouse-os-type": f"{test_os}",
                "ohouse-user-id": f"{user_id}",
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "Authorization": f"Bearer {token}"
                  }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = requests.put(url=qa_api_url, headers=header, timeout=10)#verify=False)
                if response.status_code == 204:
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

    def unfollow_hash_tag(self, tag_name, test_os, version, user_id, cookie_value, token):
        '''
                보안을 위해 제거
                '''

