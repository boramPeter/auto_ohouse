import requests, urllib3
import json
import time
from app.common.app_config.data import ApiBaseUrl
from app.api.join.sign_in import SignInApi
from app.common.base_method.api_binary import ApiBinary
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class FollowApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_api_url

    def do_follow(self, token, get_user_id, cookie_value,user_id, os_type, version):

        api_url = f"{self.api_url}/collections.json"
        qa_api_url = f"{self.qa_api_url}/user/v1/following"

        header = {
                "Content-Type": "application/json",
                "ohouse-user-id": str(get_user_id),
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "ohouse-os-type": os_type,
                "Authorization": f"Bearer {token}"

        }

        payload = {
            "os_type": os_type,
            "app": "true",
            "version": version,
            "followeeId": user_id
        }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header,timeout=10, data=json.dumps(payload))#verify=False)
                if response.status_code == 200:
                    break
                else:
                    retry_count += 1
                    time.sleep(1)
            except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                print(f"ConnectionError,ProtocolError 발생: {e}")
                retry_count += 1
                time.sleep(1)
        else:
            raise TimeoutException(f"응답코드 : {response.status_code}로 인해 팔로우 실패")
        try:
            result = response.json()['followeeId']
            print(result)
            return result
        except IndexError as e:
            raise TimeoutException(f"follow api IndexError : {e}, api확인필요")

    def del_follow(self, token, get_user_id, cookie_value, user_id, os_type, version):
        '''
                보안을 위해 제거
                '''