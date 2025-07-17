import requests, urllib3
import json
from app.common.app_config.data import ApiBaseUrl


class WithdrawalsApi:
    def is_withdrawals_api(self, os, version, cookie_value):
        qa_base_url = ApiBaseUrl.qa_base_url
        prd_base_url = ApiBaseUrl.prd_base_url

        api_url = f"{prd_base_url}/withdrawals.json?os_type={os}&version={version}"
        qa_api_url = f"{qa_base_url}/withdrawals.json?os_type={os}&version={version}"

        payload = {
            "withdrawal": {
                "reasons": [
                    0
                ],
                "reason_detail": ""
            }
        }

        # 응답 헤더에서 쿠키 값을 추출

        api_headers = {
            "Content-Type": "application/json",
            'Cookie': f'_ohouse_session_4={cookie_value}'
        }

        api_response = requests.post(url=qa_api_url, headers=api_headers, data=json.dumps(payload))#verify=False)

        # 여기서부터는 api_response를 사용하여 필요한 작업을 수행
        print(api_response)
