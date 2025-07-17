import requests
import time

# 환경 변수에서 토큰과 채널ID를 불러오는 방식 (보안상 권장)
SLACK_BOT_TOKEN = ""
SLACK_CHANNEL_ID = ""

MAX_SLACK_MESSAGE_LENGTH = 40000
MAX_RETRIES = 3
RETRY_WAIT_SECONDS = 10

def send_slack_message(message: str):
    """
    Slack 메시지를 40000자 이하로 분할해 순차 전송.
    429 에러 발생 시 최대 3회까지 재시도하며, 각 재시도는 10초 후 실행.
    """
    if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
        raise ValueError("SLACK_BOT_TOKEN 또는 SLACK_CHANNEL_ID가 설정되어 있지 않습니다.")

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    chunks = [message[i:i + MAX_SLACK_MESSAGE_LENGTH] for i in range(0, len(message), MAX_SLACK_MESSAGE_LENGTH)]

    for idx, chunk in enumerate(chunks, 1):
        retries = 0
        while retries < MAX_RETRIES:
            data = {
                "channel": SLACK_CHANNEL_ID,
                "text": chunk
            }
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200 and response.json().get("ok"):
                print(f"({idx}/{len(chunks)}) 메시지 전송 완료")
                break
            elif response.status_code == 429:
                print(f"429 Rate Limited: {RETRY_WAIT_SECONDS}초 후 재시도... ({retries + 1}/{MAX_RETRIES})")
                time.sleep(RETRY_WAIT_SECONDS)
                retries += 1
            else:
                raise Exception(f"Slack 메시지 전송 실패: {response.text}")
        else:
            raise Exception(f"최대 재시도 횟수 초과: ({idx}/{len(chunks)}) 전송 실패")
