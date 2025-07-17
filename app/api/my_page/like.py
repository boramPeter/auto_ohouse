import requests, urllib3
import json
import time
from app.common.app_config.data import ApiBaseUrl
from app.api.join.sign_in import SignInApi
from app.common.base_method.api_binary import ApiBinary
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class LikeApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def read_like(self, email, pw, os, version):
        get_token_id = SignInApi().is_sign_in(email, pw)

        ApiBinary().write_binary("token", get_token_id[0])
        token = ApiBinary().read_binary("token")
        print(token)

        ApiBinary().write_binary("user_id", get_token_id[2])
        user_id = ApiBinary().read_binary("user_id")
        print(user_id)

        api_url = f"{self.api_url}/users/{user_id}/praises.json?app=true&os_type={os}&v=2&version={version}"
        qa_api_url = f"{self.qa_api_url}/users/{user_id}/praises.json?app=true&os_type={os}&v=2&version={version}"

        header = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
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
        praise_id = response.json()['praise'][0]['id']
        praise_type = response.json()['praise'][0]['type']
        result = [praise_id, praise_type]

        return result

    def like_cancle(self, email, pw, os, version):
        '''
                보안을 위해 제거
                '''

