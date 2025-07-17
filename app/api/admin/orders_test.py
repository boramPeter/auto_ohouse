from app.common.app_config.data import ApiBaseUrl
import time,json,ssl
import http.client
import urllib.parse
from app.api.admin.admin_login import AdminLoginClass

context = ssl._create_unverified_context()  # 인증서 검증 비활성화


class OrderTestClass:
    def __init__(self):
        self.qa_admin_test_order = ApiBaseUrl.qa_admin_test_order
    '''
    - order_status -
    결제완료 : PAYMENT_COMPLETE
    배송준비 : READY_FOR_DELIVERY
    배송중 : ON_DELIVERY
    배송완료 : DELIVERY_COMPLETE
    구매확정 : CONFIRMED
    '''
    def do_test_order(self,order_status,user_id,item_no,option_no,order_count):
        qa_admin_test_order = self.qa_admin_test_order
        parsed_url = urllib.parse.urlparse(qa_admin_test_order)
        jwt = AdminLoginClass().get_jwt_admin()
        headers = {
            "x-ohouse-jwt": jwt,
            "Content-Type": "application/json"
        }
        data = {
                "orderStatus": order_status,
                "orderCount": 1,
                "goodsOptionListText": f"{item_no},{option_no},{order_count}",
                "userId": int(user_id),
                "goodsOptionList": [{
                    "goodsId": item_no,
                    "goodsOptionId": option_no,
                    "count": order_count
                }]
            }

        encoded_data = json.dumps(data)
        max_retries = 3  # 최대 재시도 횟수
        retry_count = 0

        while retry_count < max_retries:
            try:
                conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=10, context=context)  # HTTPS 연결

                conn.request("POST", parsed_url.path, body=encoded_data, headers=headers)  # 요청 보내기
                response = conn.getresponse()  # 응답 받기
                response_body = response.read().decode()

                response_json = json.loads(response_body)
                print(response_body,response_json)
                result = response_json.get("success", None)  # "oneTimePassword" 값 추출
                conn.close()  # 연결 닫기
                return result
            except Exception as e:
                print(f"Request failed: {e}")
                retry_count += 1


