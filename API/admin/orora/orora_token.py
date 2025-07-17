import asyncio
import time
from API.admin.orora.admin_login import get_token

TOKEN = None
TOKEN_TIMESTAMP = 0  # 토큰 생성 시간
TOKEN_EXPIRE_TIME = 3600  # 토큰 유효기간 (예: 1시간)

async def orora_token():
    """ 기존 토큰이 없거나 만료되었을 때 새로운 토큰을 가져오는 함수 """
    global TOKEN, TOKEN_TIMESTAMP

    current_time = time.time()
    print(f"현재 토큰 상태: {TOKEN}, 만료 시간: {TOKEN_TIMESTAMP}, 현재 시간: {current_time}")

    if TOKEN is None or (current_time - TOKEN_TIMESTAMP) >= TOKEN_EXPIRE_TIME:
        new_token = await get_token()

        if new_token:  # 새로운 토큰이 정상적으로 반환되었는지 확인
            TOKEN = new_token
            TOKEN_TIMESTAMP = time.time()
            print(f"새로운 토큰 저장: {TOKEN}, 갱신된 타임스탬프: {TOKEN_TIMESTAMP}")
        else:
            print("⚠get_token()에서 None이 반환됨. 기존 토큰 유지.")

    return TOKEN


