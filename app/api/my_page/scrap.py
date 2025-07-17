import requests, urllib3
import json
import time
from app.common.app_config.data import ApiBaseUrl
from app.api.join.sign_in import SignInApi
from app.common.base_method.api_binary import ApiBinary
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError


class ScrapApi:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    def do_scrap(self, token, get_user_id, cookie_value,collectible_id, collectible_type, os_type, version,folder_id=None):

        api_url = f"{self.api_url}/collections.json"
        qa_api_url = f"{self.qa_api_url}/collections.json"

        header = {
                "Content-Type": "application/json",
                "ohouse-user-id": str(get_user_id),
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "ohouse-os-type": os_type,
                "Authorization": f"Bearer {token}"

        }
        if folder_id is not None:
            payload = {
                        "os_type": os_type,
                        "version": version,
                        "collection": {
                            "collection_book_id": folder_id,
                            "collectible_id": collectible_id,
                            "collectible_type": collectible_type
                        },
                        "app": "true"
                    }
        else:
            payload = {
                "collection": {
                    "collectible_id": collectible_id,
                    "collectible_type": collectible_type
                    },
                "os_type": os_type,
                "app": "true",
                "version": version
                }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header,timeout=10, data=json.dumps(payload))#verify=False)
                if response.status_code == 200:
                    print(response.text)
                    break
                else:
                    retry_count += 1
                    time.sleep(1)
            except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                print(f"ConnectionError,ProtocolError 발생: {e}")
                retry_count += 1
                time.sleep(1)
        if retry_count == max_retries:
            print("재시도횟수 많아서 예외처리")
            raise TimeoutException
        result = response.json()['success']
        return result

    def get_scrap_folder_count(self, token, get_user_id, cookie_value,name, version):
        '''
                보안을 위해 제거
                '''


