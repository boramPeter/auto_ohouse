import subprocess
import time
import asyncio

async def restart_device(udid):
    """디바이스를 재시작하고 연결될 때까지 대기"""
    try:
        # 디바이스 재시작 실행
        process = await asyncio.create_subprocess_exec(
            "idevicediagnostics", "-u", udid, "restart",
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        await process.communicate()
        print(f"{udid} 재시작 완료. 연결 대기 중...")

        # 최대 60초 동안 연결 확인
        start_time = time.time()
        while time.time() - start_time < 60:
            if await is_device_connected(udid):
                print(f"{udid} 재연결 완료!")
                return {"status": "success", "udid": udid}

            await asyncio.sleep(2)  # 2초 대기 후 다시 확인

        print(f"{udid} 재시작 후 연결 실패")
        return {"status": "failed", "udid": udid}

    except Exception as e:
        print(f"⚠️ 에러 발생: {e}")
        return {"status": "error", "message": str(e)}

async def is_device_connected(udid):
    """디바이스 연결 상태 확인 (비동기)"""
    try:
        process = await asyncio.create_subprocess_exec(
            "ideviceinfo", "-u", udid,
            stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL
        )
        return await process.wait() == 0
    except Exception:
        return False