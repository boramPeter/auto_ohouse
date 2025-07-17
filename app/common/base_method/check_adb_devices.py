import subprocess
from app.common.app_config.data import UDID


def check_adb_device(device_ip_port):
    """ADB로 특정 기기의 연결 상태를 확인하는 함수"""
    try:
        # adb devices 명령 실행
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)

        # 결과에서 특정 기기의 IP:PORT 포함 여부 확인
        for line in result.stdout.splitlines():
            if device_ip_port in line:
                if "device" in line:
                    print(f"{device_ip_port} 연결됨")
                    return True
                elif "unauthorized" in line:
                    print(f"{device_ip_port} 인증안됨")
                    return False
                elif "offline" in line:
                    print(f"{device_ip_port} 연결풀림")
                    return False
        print(f"{device_ip_port} 연결되지 않음")
        return False

    except Exception as e:
        print(f"에러 발생: {e}")
        return False


def disconnect_device(device_ip_port):
    try:
        result = subprocess.run(["adb", "disconnect", device_ip_port], capture_output=True, text=True)
        if "disconnected" in result.stdout.lower():
            print(f"{device_ip_port} 연결 해제 성공")
            return True
        else:
            print(f"{device_ip_port} 연결 해제 실패: {result.stdout.strip()}")
            return False
    except Exception as e:
        print(f"disconnect_device 에러 발생: {e}")
        return False

