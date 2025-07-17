import requests, urllib3
import json
import re
import time
from app.common.app_config.data import ApiBaseUrl
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError
import urllib.parse
from app.common.base_method.ios_result_binary import Result
from app.common.base_method.aos_result_binary import ResultAndroid

class SignUpAPI:
    def verification_email_post(self, version, os_type, email):
        qa_base_url = ApiBaseUrl.qa_base_url
        qa_verification_url = f"{qa_base_url}/verification/email.json"

        prd_base_url = ApiBaseUrl.prd_base_url
        verification_url = f"{prd_base_url}/verification/email.json"

        header = {"Content-Type": "application/json"}
        post_qa_payload = {
                "version": version,
                "os_type": os_type,
                "app": "true",
                "email": email
                }

        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0
        response = None
        while retry_count < max_retries:
            try:
                response = requests.post(url=qa_verification_url, headers=header,timeout=10, data=json.dumps(post_qa_payload))#verify=False)
                if response.status_code == 200:
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
            raise TimeoutException("재시도횟수 많아서 예외처리")

        # 200에러 확인필요 + gmail 인증번호 호출함수 필요
        print(response.status_code)
        cookie_match = re.search(r'_ohouse_session_4=([^;]+)', response.headers.get('Set-Cookie', ''))
        cookie_value = cookie_match.group(1)

        return cookie_value
    def verification_email_put(self, cookie_value, auth_code, version, os_type, email):
        '''
                보안을 위해 제거
                '''




