from API.config.url import URLS
import asyncio
import aiohttp,ssl
import json
import urllib.parse
from API.admin.orora.admin_login import get_token
from API.admin.orora.orora_token import orora_token
from datetime import datetime, timedelta
import re




context = ssl._create_unverified_context()  # 인증서 검증 비활성화

# 현재 날짜
today = datetime.today()
# 한 달 전 날짜
one_month_ago = today - timedelta(days=30)
#일주일 전 날짜 
week_ago = today- timedelta(days=7)

paymentAtFrom = one_month_ago.strftime("%Y-%m-%d")
paymentAtTo = today.strftime("%Y-%m-%d")
week_ago_day = week_ago.strftime("%Y-%m-%d")


class OroraOrdersClass:
    def __init__(self):
        self.orora = URLS["orora"]

    async def get_orora_option_id(self,order_id):
        base_url = self.orora
        orora_option = f"{base_url}/orora/order/v1/orora/orders"
        parsed_url = urllib.parse.urlparse(orora_option)
        token = await orora_token()
        if token is None:
            print(f"get_orora_option_id에서 token 생성안됨 재생성 시도.")
            await orora_token()
        print(f"get_orora_option_id token : {token}")
        headers = {"Content-Type": "application/json", "authorization": f"Bearer {token}"}
        data = {
                "filters": {
                    "statuses": ["PAYMENT_COMPLETE", "READY_FOR_DELIVERY", "ON_DELIVERY", "DELIVERY_COMPLETE", "CONFIRMED"],
                    "carrierTypes": ["PARCEL_SERVICE", "CARGO_SERVICE", "SELLER_DIRECT", "RETAIL", "FAST_APPLIANCE", "FAST_FURNITURE"],
                    "orderId": order_id,
                    "paymentAtFrom": paymentAtFrom,
                    "paymentAtTo": paymentAtTo
                },
                "page": {
                    "cursor": None,
                    "direction": "NEXT",
                    "size": 50
                },
                "order": "PAYMENT_AT_DESC"
            }
        encoded_data = json.dumps(data)
        print(f"get_orora_option_id data : {encoded_data}")
        max_retries = 3
        retry_count = 0

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            while retry_count < max_retries:
                try:
                    async with session.post(
                            parsed_url.geturl(), data=encoded_data, headers=headers, timeout=10
                    ) as response:

                        response_body = await response.text()
                        response_json = json.loads(response_body)
                        orders = response_json.get("orders", [])

                        result = [
                            (order.get("orderOptionId",None), order.get("statusDesc",None), order.get("deliveryMethodDesc",None))
                            for order in orders
                        ]
                        print(f"get_orora_option_id response json:{response_json},{orders},{result}")

                        return result
                except Exception as e:
                    print(f"Request get_orora_option_id failed: {e}")
                    retry_count += 1
        return None

    async def input_invoice(self,option_id):
        base_url = self.orora
        orora_option = f"{base_url}/orora/order/v1/orora/orders/options/{option_id}/invoice"
        parsed_url = urllib.parse.urlparse(orora_option)

        headers = {"Content-Type": "application/json", "authorization": f"Bearer {await orora_token()}"}
        data = {
                "deliveryCompanyCode": "CJ_GLS",
                "invoiceNo": "1234567890"
            }
        encoded_data = json.dumps(data)

        max_retries = 3
        retry_count = 0

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            while retry_count < max_retries:
                try:
                    async with session.post(
                            parsed_url.geturl(), data=encoded_data, headers=headers, timeout=10
                    ) as response:
                        if response.status == 200:
                            print("input_invoice complete")
                            return True
                except Exception as e:
                    print(f"Request input_invoice failed: {e}")
                retry_count += 1
        return False

    '''
        보안을 위해 제거
        '''


