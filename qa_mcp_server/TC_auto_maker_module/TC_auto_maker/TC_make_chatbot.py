import google.generativeai as genai
from qa_mcp_server.qa_scope_module.token_manager import APIKeyManager
from typing import List, Dict, Optional

# key_manager = APIKeyManager()

# api_key = key_manager.get_key()
# print(api_key)
genai.configure(api_key="AIzaSyBsKkgCQy0rb4sJzaZYp8WnhKmqu5PQ9-U")

class ScopeChatbot:
    def __init__(self,
                 document_text: Optional[str] = None,
                 initial_history: Optional[List[Dict]] = None,
                 context_id: str = "챗봇 컨텍스트",
                 model_name: str = 'gemini-2.5-pro'):#'models/gemini-2.5-flash-preview-04-17'):#'gemini-2.5-pro-exp-03-25'):
        self.model_name = model_name
        self.context_id = context_id
        self.document_text = document_text
        self.initial_history = initial_history

        if self.initial_history is not None:
            print(f"[{self.context_id}] 제공된 초기 대화 기록을 사용합니다.")
        elif self.document_text is not None:
            print(f"[{self.context_id}] 제공된 문서 텍스트로 초기 대화 기록을 생성합니다.")
            self.initial_history = self._create_initial_history_from_text(self.document_text)
            if not document_text:
                 print(f"경고 [{self.context_id}]: 문서 내용이 비어있습니다.")
                 self.initial_history = []
        else:
            print(f"경고 [{self.context_id}]: 초기 컨텍스트 정보가 없습니다. 빈 대화로 시작합니다.")
            self.initial_history = []

        try:
            self.model = genai.GenerativeModel(self.model_name)
            self.chat_session = self.model.start_chat(history=self.initial_history)
            print(f"'{self.model_name}' 모델 [{self.context_id}] 챗봇 초기화 완료.")
        except Exception as e:
            print(f"챗봇 초기화 중 오류 발생 [{self.context_id}]: {e}")
            self.model = None
            self.chat_session = None

    def _create_initial_history_from_text(self, doc_text: str) -> List[Dict]:
        # 단일 문서 기본 컨텍스트 생성 (여기서는 직접 사용되지 않음)
        return [
            {
                "role": "user",
                "parts": [{"text": f"다음 내용을 바탕으로 질문에 답해주세요:\n{doc_text}"}]
            },
            {
                "role": "model",
                "parts": [{"text": "네, 내용을 확인했습니다. 질문해주세요."}]
            }
        ]

    def send_message(self, user_prompt: str) -> Optional[str]:
        if not self.chat_session:
            print(f"오류 [{self.context_id}]: 챗봇 세션이 초기화되지 않았습니다.")
            return None
        if not user_prompt:
            print(f"오류 [{self.context_id}]: 빈 메시지는 보낼 수 없습니다.")
            return None
        try:
            print(f"\n[{self.context_id} - 사용자] {user_prompt}")
            response = self.chat_session.send_message(user_prompt)
            response_text = response.text
            print(f"[{self.context_id} - {self.model_name}] {response_text}")
            return response_text
        except Exception as e:
            print(f"메시지 전송/응답 수신 중 오류 발생 [{self.context_id}]: {e}")
            return None

    # get_history, reset_chat 메소드는 필요시 사용 (이전과 동일)
    def get_history(self) -> Optional[List[Dict]]:
        if not self.chat_session: return None
        return self.chat_session.history

    def reset_chat(self):
        if not self.model: return
        try:
            self.chat_session = self.model.start_chat(history=self.initial_history)
            print(f"[{self.context_id}] 채팅 세션 리셋 완료.")
        except Exception as e: print(f"채팅 리셋 중 오류 [{self.context_id}]: {e}")


# --- 3. 핵심 로직 함수 정의 ---
def generate_testcase(
    context_1, context_2,context_3,prompt,
    model_name: str = 'gemini-2.5-pro',# 'models/gemini-2.5-flash-preview-04-17', 'gemini-2.5-pro-exp-03-25',
    context_id: str = "패턴 적용 챗봇"
) -> Optional[str]:

    print(f"\n--- '{context_id}' 초기화 및 테스트 범위 도출 시작 ---")
    print(f"사용 모델: {model_name}")

    # --- 함수 내에서 학습 컨텍스트 동적 생성 ---
    learning_context = [
        {
            "role": "user",
            "parts": [
                {"text": f"""    
    {context_1}
                """}
            ]
        },
        {
            "role": "model",
            "parts": [
                {"text": """
                기획서 전체 내용에 대한 분석 및 이해가 완료되었습니다. 테스트 케이스 작성 준비가 되었습니다.
                """}
            ]
        },
        {
            "role": "user",
            "parts": [
                {"text": f"""
        {context_2}
                """}
            ]
        },
        {
            "role": "model",
            "parts": [
                {"text": """
                테스트 범위 문서를 통해 프로젝트의 주요 검증 포인트를 이해했습니다. 내용이 명확하게 정리되어 있어 추가적인 질문은 현재 없습니다. 다음 단계 진행을 준비하겠습니다.
                """}
            ]
        },
        {
            "role": "user",
            "parts": [
                {"text": f"""
    {context_3}
                    """}
            ]
        },
        {
            "role": "model",
            "parts": [
                {"text": """
                 테스트 범위 및 유사케이스를 학습했습니다. 준비되었습니다.
                    """}
            ]
        }
    ]
    # --- 학습 컨텍스트 생성 완료 ---

    # 학습된 컨텍스트로 챗봇 인스턴스 생성
    chatbot = ScopeChatbot(
        initial_history=learning_context, # 함수 내에서 생성한 컨텍스트 전달
        context_id=context_id,
        model_name=model_name
    )

    # 챗봇 초기화 성공 여부 확인
    if not chatbot.chat_session:
        print(f"오류: '{context_id}' 초기화 실패.")
        return None

    # 모델에게 새로운 문서 내용 전달 및 테스트 범위 도출 요청 메시지 구성
    user_request = f"""
        {prompt}
    """

    # 챗봇에게 메시지 전송 및 응답 받기
    response = chatbot.send_message(user_request)

    print(f"--- '{context_id}' 테스트케이스 생성 완료 ---")
    return response


# --- 4. 메인 실행 부분 ---
if __name__ == "__main__":
    keys = ["AIzaSyBJXmuqL1lBC3lHM9WmwDJDgbBBZzUtGAw", "AIzaSyB576Y-Ke0e7sikSq3wmh9cOI4vuOX9X1M",
            "AIzaSyCP3r0gIZa_44713E2-u4UBaf5AIUYCGBc"]
    key_manager = APIKeyManager(keys)

    api_key = key_manager.print_status()
    print(api_key)