# from app.common.base_method.proxy import SetMitmproxy
from mitmproxy import http
import json

TARGET_URL = ""

def response(flow: http.HTTPFlow):
    # URL과 쿼리까지 정확히 매칭
    if flow.request.pretty_url.startswith(TARGET_URL):
        # 응답이 JSON인지 확인
        if "application/json" in flow.response.headers.get("content-type", ""):
            try:
                data = json.loads(flow.response.text)
                # "requestId"가 있으면 저장
                request_id = data.get("requestId")
                if request_id:
                    with open("request_id.txt", "w", encoding="utf-8") as f:
                        f.write(request_id)
                    print(f"requestId 저장됨: {request_id}")
            except Exception as e:
                print(f"JSON 파싱 오류: {e}")