import time
import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError
from app.api.join.sign_in import SignInApi

class MoveCloseAPI:
    def __init__(self):
        self.api_url = ApiBaseUrl.prd_base_url
        self.qa_api_url = ApiBaseUrl.qa_base_url

    #
    def close_bottom_sheet_api(self, email, password,pw2=None):
        code = SignInApi().get_user_id(email, password,pw2=pw2)[0]
        if code == 200:
            result = SignInApi().is_sign_in(email, password)
            token = result[0]
            cookie_value = result[1]
            user_id = result[2]
        else:
            print(f"close_bottom_sheet_api : {code}")
            raise TimeoutException("get_user_id api 200안떨어짐. api 확인필요")


        qa_api_url = ""

        header = {
                "Content-Type": "application/json",
                "ohouse-os-type":"iOS",
                "ohouse-user-id": f"{user_id}",
                'Cookie': f'_ohouse_session_4={cookie_value}',
                "authorization": f"Bearer {token}"
                  }

        payload = {
                    "responseType": "CANCEL",
                    "id": "myPageLifeEvent"
                }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header, timeout=10,
                                         data=json.dumps(payload))  # verify=False)
                if response.status_code == 204:
                    break
                else:
                    retry_count += 1
                    time.sleep(1)
            except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                print(f"ConnectionError,ProtocolError 발생: {e}")
                retry_count += 1
                time.sleep(1)
        else:
            raise TimeoutException(f"응답코드 : {response.status_code}로 인해 바텀시트 종료 실패")