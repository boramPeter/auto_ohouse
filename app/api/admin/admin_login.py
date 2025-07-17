from app.common.app_config.data import ApiBaseUrl
import time,json,ssl
import http.client
import urllib.parse
context = ssl._create_unverified_context()  # 인증서 검증 비활성화


class AdminLoginClass:
    def __init__(self):
        self.login_api = ApiBaseUrl.qa_admin_login_api
        self.otp_api = ApiBaseUrl.qa_admin_otp_api
        self.jwt_api = ApiBaseUrl.qa_admin_jwt_api
        self.portal_api = ApiBaseUrl.qa_admin_portal_api

    def get_login_code(self, id, pw):
        login_api = self.login_api  # URL 추출
        parsed_url = urllib.parse.urlparse(login_api)  # URL 파싱

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "login_id": id,
            "password": pw,
            "redirect_uri": "https://admin-portal.qa.dailyhou.se/commerce/product/deals_new?remember_me=false",
            "response_type": "code"
        }

        encoded_data = urllib.parse.urlencode(data)  # 데이터 URL 인코딩
        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0

        while retry_count < max_retries:
            try:
                conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=10, context=context)  # HTTPS 연결

                conn.request("POST", parsed_url.path, body=encoded_data, headers=headers)  # 요청 보내기
                response = conn.getresponse()  # 응답 받기
                location_url = response.getheader("location")
                parsed_location = urllib.parse.urlparse(location_url)
                query_params = urllib.parse.parse_qs(parsed_location.query)  # 쿼리 파라미터 파싱
                code_value = query_params.get("code", [None])[0]
                conn.close()  # 연결 닫기
                return code_value
            except Exception as e:
                print(f"Request failed: {e}")
                retry_count += 1

    '''
            보안을 위해 제거
            '''