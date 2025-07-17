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
yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")



#오로라 > 정산 
class SettlementClass:

    def __init__(self):
        self.orora = URLS["orora"]
        self.partner = URLS["partner"]

    #정산 > 정산 파트너 전용 session 생성
    async def get_partner_orora_token(self):
        base_url = self.orora
        url = f"{base_url}/orora/member/v1/legacy/users/orora-token"
        token = await orora_token()

       
        headers = {
            "authorization": f"Bearer {token}"
            }
    

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            for _ in range(3):
                try:
                    async with session.get(url,headers=headers,timeout=10) as response:
                        if response.status == 200:
                            print(f"get_partner_orora_token 응답값 : {response.status}")
                            response_json = json.loads(await response.text())
                            #payload 값만 리턴
                            payload = response_json.get("payload")
                            return payload
                        print(f"get_partner_orora_token 에러 : {response.status}")
                except Exception as e:
                    print(f"get_partner_orora_token exception error :{e}")
        return False   



    #정산 파트너사 세션 생성

    '''
            보안을 위해 제거
            '''

    
    
