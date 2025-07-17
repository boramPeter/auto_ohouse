import google.generativeai as genai
from qa_mcp_server.qa_scope_module.token_manager import APIKeyManager
from typing import List, Dict, Optional
import PIL.Image


class ScopeChatbot:
    def __init__(self,
                 document_text: Optional[str] = None,
                 initial_history: Optional[List[Dict]] = None,
                 context_id: str = "챗봇 컨텍스트",
                 model_name: str = 'gemini-2.5-pro'):
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
def generate_test_scope(
    new_doc_text: str = None,
    photo_path: list = None,
    model_name: str = 'gemini-2.5-pro',
    context_id: str = "패턴 적용 챗봇"
) -> Optional[str]:
    '''
    로직 제거.
    '''