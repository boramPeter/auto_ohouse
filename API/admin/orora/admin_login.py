from API.config.url import URLS
import asyncio
import aiohttp,ssl
import json
import urllib.parse

context = ssl._create_unverified_context()  # 인증서 검증 비활성화

class OroraClass:
    def __init__(self):
        self.orora = URLS["orora"]

    async def get_orora_account_id(self):
        base_url = self.orora
        orora_login = f"{base_url}/orora/member/v1/auth"
        parsed_url = urllib.parse.urlparse(orora_login)

        headers = {"Content-Type": "application/json", "authorization": "Bearer null"}
        data = {"email": "test01@test.com", "password": "qwer1234!"}
        encoded_data = json.dumps(data)

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
                        account_id = response_json.get("accountId", "10823919")
                        return account_id
                except Exception as e:
                    print(f"Request get_orora_account_id failed: {e}")
                    retry_count += 1
        return None

    async def mfa_1(self, account_id):
        base_url = self.orora
        orora_mfa = f"{base_url}/orora/member/v1/auth/mfa"
        parsed_url = urllib.parse.urlparse(orora_mfa)

        headers = {"Content-Type": "application/json", "authorization": "Bearer null"}
        data = {"destination": "test01@test.com", "type": "EMAIL_FOR_SIGN_IN", "partnerId": account_id}
        encoded_data = json.dumps(data)

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
                        return response_json.get("success", False)
                except Exception as e:
                    print(f"Request mfa_1 failed: {e}")
                    retry_count += 1
        return False

    async def mfa_2(self):
        base_url = self.orora
        orora_mfa = f"{base_url}/orora/member/v1/auth/mfa"
        parsed_url = urllib.parse.urlparse(orora_mfa)

        headers = {"Content-Type": "application/json", "authorization": "Bearer null"}
        data = {
                "destination": "test01@test.com",
                "verificationCode": "123456"
            }
        encoded_data = json.dumps(data)

        max_retries = 3
        retry_count = 0

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            while retry_count < max_retries:
                try:
                    async with session.put(
                            parsed_url.geturl(), data=encoded_data, headers=headers, timeout=10
                    ) as response:
                        response_body = await response.text()
                        response_json = json.loads(response_body)
                        return response_json.get("success", False)
                except Exception as e:
                    print(f"Request mfa_2 failed: {e}")
                    retry_count += 1
        return False

    async def get_access_token(self,accoun_id):
        base_url = self.orora
        orora_access = f"{base_url}/orora/member/v1/auth/access-token"
        parsed_url = urllib.parse.urlparse(orora_access)

        headers = {"Content-Type": "application/json", "authorization": "Bearer null"}
        data = {
                "accountId": accoun_id,
                "verificationCode": "123456",
                "destination": "test01@test.com"
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
                        cookies = response.headers.get("Set-Cookie", "")
                        token = None
                        for cookie in cookies.split("; "):
                            if cookie.startswith("_orora_partner_session="):
                                token = cookie.split("=")[1]
                                break
                        return token
                except Exception as e:
                    print(f"Request get_access_token failed: {e}")
                    retry_count += 1
        return token
    async def get_orora_token(self,token):
        base_url = self.orora
        orora_access = f"{base_url}/orora/member/v1/legacy/users/orora-token"
        parsed_url = urllib.parse.urlparse(orora_access)

        headers = {"Content-Type": "application/json", "authorization": f"Bearer {token}"}


        max_retries = 3
        retry_count = 0

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            while retry_count < max_retries:
                try:
                    async with session.get(
                            parsed_url.geturl(),headers=headers, timeout=10
                    ) as response:
                        response_body = await response.text()
                        response_json = json.loads(response_body)
                        return response_json.get("payload", False)
                except Exception as e:
                    print(f"Request get_orora_token failed: {e}")
                    retry_count += 1
        return False
    async def is_accounts(self,token):
        base_url = self.orora
        orora_access = f"{base_url}/orora/member/v1/accounts"
        parsed_url = urllib.parse.urlparse(orora_access)

        headers = {"Content-Type": "application/json", "authorization": f"Bearer {token}"}

        max_retries = 3
        retry_count = 0

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=context)) as session:
            while retry_count < max_retries:
                try:
                    async with session.get(
                            parsed_url.geturl(), headers=headers, timeout=10
                    ) as response:
                        response_body = await response.text()
                        response_json = json.loads(response_body)
                        return response_json.get("payload", False)
                except Exception as e:
                    print(f"Request is_accounts failed: {e}")
                    retry_count += 1
        return False
async def get_token():
    orora = OroraClass()
    account_id = await orora.get_orora_account_id()
    success_1 = await orora.mfa_1(account_id)
    if success_1:
        success_2 = await orora.mfa_2()
        if success_2:
            token = await orora.get_access_token(account_id)
            if token is not None:
                # 안쓰는 토큰인것으로 보임
                # orora_token, _ = await asyncio.gather(orora.get_orora_token(token), orora.is_accounts(token))
                await orora.get_access_token(token)
                return token
    return None
# print(asyncio.run(get_token()))