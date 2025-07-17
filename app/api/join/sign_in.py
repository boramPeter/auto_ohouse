import requests, urllib3
import json
import re
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from requests.exceptions import JSONDecodeError
from app.common.app_config.data import AppVersion
from urllib3.exceptions import ProtocolError

class SignInApi:
    def is_sign_in(self, email, pw):
        prd_base_url = ApiBaseUrl.prd_base_url
        api_url = f"{prd_base_url}/users/sign_in.json"

        qa_base_url = ApiBaseUrl.qa_base_url
        qa_api_url = f"{qa_base_url}/users/sign_in.json"

        header = {
            "Content-Type": "application/json",
            "bp-cid": ""
        }
        payload= {
            "udid": "",
            "v": 2,
            "version": AppVersion.version("iOS"),
            "user": {
                "email": email,
                "password": pw
            },
            "os_type": "iOS",
            "app": "true"
        }
        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header,timeout=10, data=json.dumps(payload))#verify=False)
                print(response.json())
                break
            except (requests.exceptions.ConnectionError, ProtocolError, OSError) as e:
                print(f"ConnectionError,ProtocolError 발생: {e}")
                retry_count += 1
                time.sleep(1)
                if retry_count == retry_count:
                    raise TimeoutException("ProtocolError가 3회이상 발생하여 fail")
        print(response.json())
        success = response.json()['success']
        if success == True:
            cookie_match = re.search(r'_ohouse_session_4=([^;]+)', response.headers.get('Set-Cookie', ''))
            cookie_value = cookie_match.group(1)
            print(f"_ohouse_session_4의 값: {cookie_value}")
            token = response.json()['data']['auth_token']
            user_id = response.json()['data']['user']['id']
            print([token, cookie_value, user_id, 200])
            return [token, cookie_value, user_id, 200]
        else:
            #retry_count += 1
            return [None, None, None, 400]
        # if retry_count == max_retries:
        #     return [None, None, None,400]




    def get_user_id(self, email, pw,pw2=None):
        print(f"get_user_id 시작 : {email,pw,pw2}")
        prd_base_url = ApiBaseUrl.prd_base_url
        api_url = f"{prd_base_url}/users/sign_in.json"

        qa_base_url = ApiBaseUrl.qa_base_url
        qa_api_url = f"{qa_base_url}/users/sign_in.json"

        header = {"Content-Type": "application/json"}
        payload= {
            "user": {
                "email": email,
                "password": pw
            },
            "app": "true",
            "version": AppVersion.version("iOS"),
            "v": 2
        }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        used_alternate_pw = False  # pw2를 사용했는지 여부

        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_api_url, headers=header,timeout=10, data=json.dumps(payload))#verify=False)
                success = response.json()['success']

                if success:
                    status_code = 200
                    user_id = response.json()['data']['user']['id']
                    return [status_code, user_id]

                else:
                    print(f"get_user_id 에러: {response.json()}")
                    if not used_alternate_pw:
                        # pw2로 비밀번호 변경 후 재시도
                        payload["user"]["password"] = pw2
                        used_alternate_pw = True
                    else:
                        # 이미 pw2 사용했으면 더 이상 시도하지 않음
                        return [400, None]

            except json.decoder.JSONDecodeError as e:
                # JSON 디코딩 오류 처리
                print(f"JSON 디코딩 오류: {e}")
                return [500, None]  # 리스폰스 코드를 500으로 설정

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
        print("재시도 횟수 초과")
        return [503, None]  # 재시도 횟수 초과 시 리스폰스 코드를 503으로 설정



