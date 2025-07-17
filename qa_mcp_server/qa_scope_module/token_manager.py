from datetime import datetime
import os,json
import pytz

KEYS = [
        ]

class APIKeyManager:
    def __init__(self, state_file: str = "qa_mcp_server/qa_scope_module/api_key_state.json"):
        self.keys = KEYS
        self.state_file = state_file
        self.max_calls_per_key = 25
        self.timezone = pytz.timezone('America/Los_Angeles')  # PDT/PST 자동 처리

        self._load_state()

    def _load_state(self):
        if not os.path.exists(self.state_file):
            self.state = {
                "current_key_index": 0,
                "key_call_counts": [0] * len(self.keys),
                "last_reset_date": self._current_pdt_date()
            }
            self._save_state()
        else:
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
            self._maybe_reset_counts()

    def _save_state(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f)

    def _current_pdt_date(self):
        now_pdt = datetime.now(self.timezone)
        return now_pdt.strftime("%Y-%m-%d")

    def _maybe_reset_counts(self):
        today = self._current_pdt_date()
        if self.state.get("last_reset_date") != today:
            print("[APIKeyManager] 날짜 변경 감지. 카운트 리셋합니다.")
            self.state["key_call_counts"] = [0] * len(self.keys)
            self.state["current_key_index"] = 0
            self.state["last_reset_date"] = today
            self._save_state()

    def get_key(self):
        self._maybe_reset_counts()  # 매번 호출시 날짜 체크
        idx = self.state["current_key_index"]

        # 현재 키 사용횟수 확인
        if self.state["key_call_counts"][idx] >= self.max_calls_per_key:
            idx += 1
            if idx >= len(self.keys):
                raise Exception("사용 가능한 API 키가 모두 소진되었습니다.")
            self.state["current_key_index"] = idx

        self.state["key_call_counts"][idx] += 1
        self._save_state()

        return self.keys[idx]


def print_status(state_file: str = "qa_mcp_server/qa_scope_module/api_key_state.json"):
    keys = KEYS
    try:
        with open(state_file, 'r') as f:
            state = json.load(f)
    except FileNotFoundError:
        state = {
            "key_call_counts": [0] * len(keys),
            "current_key_index": 0,
            "last_reset_date": None
        }

    # 🔥 여기서 -1 해서 반영
    new_call_counts = [max(count - 1, 0) for count in state["key_call_counts"]]
    state["key_call_counts"] = new_call_counts

    # 🔥 반영한 state를 다시 저장
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=4)

    # 이제 출력용 문장 만들기
    status_lines = ["[🔑 API Key 사용 현황]"]
    for i, (key, count) in enumerate(zip(keys, new_call_counts)):
        current = " <-- 현재 사용중" if i == state["current_key_index"] else ""
        status_lines.append(f"[{i+1}번째 키] 호출 {count}회 / {25}회{current}")
    status_lines.append(f"📅 마지막 초기화 날짜 (PDT/PST 기준): {state['last_reset_date']}")

    status_message = "ㄱ".join(status_lines)
    return status_message.replace("ㄱ", "\n\n")



