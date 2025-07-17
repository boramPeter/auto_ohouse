import json
import time,sys,os,re
import asyncio,pprint
from contextlib import AsyncExitStack
from typing import List, Dict, Any, Optional
import traceback
import streamlit as st
from dotenv import load_dotenv
import getpass
import tempfile
from datetime import datetime, timedelta
from qa_mcp_server.figma.get_data_figma import FIGMA_TOKEN_CREATION_DATE
import uuid


class DynamicMCPClient:
    def __init__(self, server_configs: List[Dict[str, Any]]):
        self.server_configs = server_configs
        self.openai = None

        # API 키 확인 및 OpenAI 클라이언트 초기화
        if GOOGLE_API_KEY:
            try:
                self.openai = OpenAI(
                    api_key=GOOGLE_API_KEY,
                    base_url="https://generativelanguage.googleapis.com/v1beta/",
                )
                print("OpenAI (Google AI) 클라이언트 초기화 성공")
            except Exception as e:
                 # 초기화 실패 시 Streamlit UI에 오류 표시 (앱 시작 시)
                 st.error(f"🚨 OpenAI (Google AI) 클라이언트 초기화 실패: {e}")
                 print(f"OpenAI (Google AI) 클라이언트 초기화 실패: {e}")
        else:
            # API 키 누락 시 Streamlit UI에 오류 표시 (앱 시작 시)
            # 입력 필드는 사이드바에서 처리
            print("경고: Google AI API 키가 설정되지 않았습니다.")
            # self.openai 는 None 상태로 유지됨

    async def process_query(self,
                            original_user_query: str,  # 명확성을 위해 변수명 변경
                            chat_history: List[Dict[str, Any]],
                            status_placeholder: Optional[Any] = None  # DeltaGenerator 대신 Any
                            ) -> Dict[str, Any]:
        # --- OpenAI 클라이언트 및 설정값 확인 (실제 __init__ 로직 필요) ---
        if not hasattr(self, 'openai') or not self.openai:
            print("경고: OpenAI 클라이언트가 self.openai로 초기화되지 않았습니다. (process_query)")
            return {"final_text": "오류: Google AI 클라이언트가 초기화되지 않았습니다.", "tool_status": []}

        # MODEL_NAME, MAX_TOKENS는 클래스 멤버 또는 전역 변수로 접근 가능해야 함
        # 이 예시에서는 전역 상수를 사용한다고 가정 (실제 코드에 맞게 조정)
        # global MODEL_NAME, MAX_TOKENS

        print("--- DynamicMCPClient.process_query 시작됨 ---")
        print(f"현재 로드된 서버 설정 (self.server_configs): {self.server_configs}")

        # 최종 반환될 LLM 텍스트 및 누적된 도구 상태 메시지
        final_llm_conclusion_text = "[LLM 최종 결론 없음]"
        accumulated_tool_status_messages: List[str] = []

        sessions: Dict[str, Any] = {}  # ClientSession
        server_tools_map: Dict[str, List[Any]] = {}  # types.Tool
        connection_errors: List[str] = []

        async with AsyncExitStack() as exit_stack:
            print(f"\n--- AsyncExitStack 진입 ---")
            print(f"--- MCP 서버 연결 시도 ({len(self.server_configs)}개) ---")
            connect_start_time = time.monotonic()

            for config in self.server_configs:
                server_id = config["id"]
                server_params_obj = config["params"]  # StdioServerParameters 객체

                print(f"  [디버그] 서버 ID '{server_id}' 연결 시도 시작. 파라미터: {server_params_obj}")
                try:
                    print(f"    [디버그] stdio_client 호출 예정 ({server_id})...")
                    stdio_transport = await exit_stack.enter_async_context(
                        stdio_client(server_params_obj)  # 실제 stdio_client 함수
                    )
                    print(f"    [디버그] stdio_client 호출 완료 ({server_id})")

                    print(f"    [디버그] ClientSession 생성 예정 ({server_id})...")
                    session = await exit_stack.enter_async_context(
                        ClientSession(*stdio_transport)  # 실제 ClientSession 클래스
                    )
                    print(f"    [디버그] ClientSession 생성 완료 ({server_id})")

                    print(f"    [디버그] session.initialize() 호출 예정 ({server_id})...")
                    await asyncio.wait_for(session.initialize(), timeout=120.0)
                    print(f"    [디버그] session.initialize() 완료 ({server_id}).")

                    print(f"    [디버그] session.list_tools() 호출 예정 ({server_id})...")
                    response = await asyncio.wait_for(session.list_tools(), timeout=60.0)
                    print(f"    [디버그] session.list_tools() 완료 ({server_id}).")

                    sessions[server_id] = session
                    server_tools_map[server_id] = response.tools
                    print(f"  ✅ '{server_id}' 연결 성공. MCP Server: {[tool.name for tool in response.tools]}")

                except asyncio.TimeoutError:
                    err_msg = f"  ⚠️ '{server_id}' 연결 시간 초과."
                    print(err_msg)
                    connection_errors.append(err_msg)
                except Exception as e:
                    err_msg = f"  ❌ '{server_id}' 연결 실패: {e}"
                    print(err_msg)
                    print(f"  [디버그] 상세 트레이스백 ({server_id}):")
                    traceback.print_exc()
                    connection_errors.append(err_msg)
                print(f"  [디버그] 서버 ID '{server_id}' 연결 시도 종료.")

            connect_end_time = time.monotonic()
            print(f"--- 서버 연결 시도 완료 (소요 시간: {connect_end_time - connect_start_time:.2f}초) ---")
            print(f"--- 성공적으로 연결된 서버: {list(sessions.keys())} ---")

            if 'st' in sys.modules:  # Streamlit 컨텍스트인지 확인
                detected_tool_names = []
                for sid, tool_list in server_tools_map.items():
                    for tool in tool_list:
                        detected_tool_names.append(f"{sid}-{tool.name}".replace("_", "-"))
                st.session_state.current_available_tools = detected_tool_names
                print(f"--- Streamlit 세션에 사용 가능 도구 저장: {detected_tool_names} ---")

            if not sessions:
                final_llm_conclusion_text = "오류: MCP Server 서버에 연결할 수 없습니다. 잠시 후 다시 시도해주세요."
                if 'st' in sys.modules:
                    st.error(final_llm_conclusion_text + "\n" + "\n".join(connection_errors))
                return {"final_text": final_llm_conclusion_text, "tool_status": []}

            # --- 반복적 LLM 호출 및 도구 실행 로직 ---
            max_iterations = 20  # 최대 반복 횟수 (너무 많으면 무한루프 가능성)
            current_iteration = 0
            task_accomplished_by_llm = False

            # LLM과의 대화 기록 (이번 process_query 내에서만 사용)
            # OpenAI 라이브러리 형식의 메시지 리스트
            iteration_messages: List[Dict[str, Any]] = []
            last_tool_result_content = None # 마지막 도구 결과 저장을 위한 변수 초기화

            # 초기 사용자 요청 구성 (OpenAI 형식)
            # chat_history의 각 메시지 content가 None이 아니도록 처리
            for i, hist_msg in enumerate(chat_history):
                role = hist_msg.get("role")
                content = hist_msg.get("content")
                tool_calls = hist_msg.get("tool_calls")

                if role == "tool":  # 도구 응답은 아래 로직에서 iteration_messages에 추가됨
                    continue

                message_to_add = {"role": role}
                processed_content = content

                if not (role == "assistant" and tool_calls):  # 도구 호출이 없는 사용자 또는 어시스턴트 메시지
                    if processed_content is None or (
                            isinstance(processed_content, str) and not processed_content.strip()):
                        processed_content = " "  # 빈 콘텐츠는 공백으로 (특히 첫 메시지)

                if processed_content is not None:
                    message_to_add["content"] = processed_content

                if role == "assistant" and tool_calls:
                    message_to_add["tool_calls"] = tool_calls
                    if content is None:  # 명시적으로 content가 None이었던 경우
                        message_to_add.pop("content", None)

                if "content" not in message_to_add and "tool_calls" not in message_to_add:
                    if role == "user" or role == "assistant":
                        message_to_add["content"] = " "  # 안전장치

                iteration_messages.append(message_to_add)

            # 현재 사용자 원본 쿼리 추가 (OpenAI 형식)
            current_query_text_for_llm = original_user_query
            if not iteration_messages:  # 첫 메시지인 경우
                if not current_query_text_for_llm or not current_query_text_for_llm.strip():
                    current_query_text_for_llm = " "
            elif current_query_text_for_llm is None:  # 첫 메시지는 아니지만 None인 경우
                current_query_text_for_llm = " "

            iteration_messages.append({"role": "user", "content": current_query_text_for_llm})

            available_tools_for_llm = self._get_combined_tools_for_llm(server_tools_map)

            try:
                while current_iteration < max_iterations and not task_accomplished_by_llm:
                    current_iteration += 1
                    print(f"\n--- 반복 실행 {current_iteration}/{max_iterations} ---")
                    if status_placeholder:
                        status_placeholder.info(f"🤖 생각 중... (단계 {current_iteration}/{max_iterations})")

                    # LLM 호출: 다음 행동 결정
                    print(f"LLM ({current_iteration}차) 호출 메시지 개수: {len(iteration_messages)}")
                    # pprint.pprint(iteration_messages) # 필요시 상세 로그

                    llm_response_obj = self.openai.chat.completions.create(
                        model=MODEL_NAME,  # 또는 self.MODEL_NAME
                        max_tokens=MAX_TOKENS,  # 또는 self.MAX_TOKENS
                        messages=iteration_messages,
                        tools=available_tools_for_llm if available_tools_for_llm else None,
                    )
                    llm_message_from_response = llm_response_obj.choices[0].message

                    # LLM 응답을 다음 반복을 위해 기록 (OpenAI 형식 그대로)
                    iteration_messages.append(llm_message_from_response.model_dump(exclude_none=True))

                    if not llm_message_from_response.tool_calls:
                        # LLM이 도구 호출 없이 직접 답변 -> 작업 완료로 간주
                        print("LLM이 최종 답변을 생성했습니다 (도구 호출 없음).")
                        final_llm_conclusion_text = llm_message_from_response.content if llm_message_from_response.content else "작업이 완료되었습니다."
                        task_accomplished_by_llm = True
                        break  # 반복 종료
                    requested_tool_calls = llm_message_from_response.tool_calls
                    print(f"LLM 요청 도구: {[tc.function.name for tc in requested_tool_calls]}")
                    if status_placeholder:
                        summary = [f"⏳ [{tc.function.name}, 인자:{tc.function.arguments}]" for tc in requested_tool_calls]
                        status_placeholder.info(f"단계 {current_iteration}: MCP server 실행 중\n" + "\n".join(summary))

                    tool_tasks_map = {}
                    tool_results_map = {}

                    # 1. 실행할 태스크 준비 또는 즉시 오류 처리
                    for tool_call in requested_tool_calls:
                        try:
                            global TOOL_ARGS  # 전역 변수 사용 선언
                            TOOL_ARGS = tool_call.function.arguments

                            tool_args = json.loads(tool_call.function.arguments)
                            task = self._find_and_call_tool(tool_call.function.name, tool_args, sessions,
                                                            server_tools_map)
                            tool_tasks_map[tool_call.id] = asyncio.create_task(task)
                        except Exception as e:
                            print(f"오류: MCP Server '{tool_call.function.name}' 호출 준비 중 오류: {e}")
                            error_content = json.dumps(
                                {"error": f"Tool call preparation or argument parsing error: {e}"})
                            tool_results_map[tool_call.id] = {"role": "tool", "tool_call_id": tool_call.id,
                                                              "name": tool_call.function.name, "content": error_content}
                            accumulated_tool_status_messages.append(f"⚠️ [{tool_call.function.name}] 호출 준비 오류")

                    # 2. 준비된 태스크들을 병렬로 실행
                    if tool_tasks_map:
                        task_items = list(tool_tasks_map.items())
                        executed_results = await asyncio.gather(*[task for _, task in task_items],
                                                                return_exceptions=True)

                        # 3. 실행된 결과를 원래의 tool_call_id와 매핑
                        for i, (tool_call_id, _) in enumerate(task_items):
                            result_obj = executed_results[i]
                            original_tool_call = next((tc for tc in requested_tool_calls if tc.id == tool_call_id),
                                                      None)
                            status_msg_for_ui = ""
                            result_content_for_llm = ""

                            if isinstance(result_obj, Exception):
                                print(f"!!! MCP Server 실행 중 오류(gather): {result_obj}")
                                error_text = json.dumps({"error": f"Tool execution error: {str(result_obj)}"})
                                result_content_for_llm = error_text
                                status_msg_for_ui = f"❌ [{original_tool_call.function.name}] 실행 오류"
                            elif isinstance(result_obj, types.CallToolResult):
                                res_text = "[결과 없음]"
                                if result_obj.content and result_obj.content[0] and isinstance(result_obj.content[0],
                                                                                               types.TextContent):
                                    res_text = result_obj.content[0].text
                                result_content_for_llm = res_text
                                status_msg_for_ui = f"✅ [{original_tool_call.function.name}] 실행 완료: {res_text[:100].replace(os.linesep, ' ')}..."
                                last_tool_result_content = result_content_for_llm
                            else:
                                error_text = json.dumps({"error": f"Unexpected result type: {type(result_obj)}"})
                                result_content_for_llm = error_text
                                status_msg_for_ui = f"❓ [{original_tool_call.function.name}] 알 수 없는 결과 타입"

                            tool_results_map[tool_call_id] = {"role": "tool", "tool_call_id": tool_call_id,
                                                              "name": original_tool_call.function.name,
                                                              "content": result_content_for_llm}
                            accumulated_tool_status_messages.append(status_msg_for_ui)

                    # 4. 원래 요청 순서대로 최종 결과 리스트 구성
                    tool_results_for_this_iteration = [tool_results_map[tc.id] for tc in requested_tool_calls]
                    iteration_messages.extend(tool_results_for_this_iteration)

                    # 루프의 끝, 다음 반복으로
                    if task_accomplished_by_llm:  # LLM이 스스로 완료를 선언한 경우
                        print(f"LLM이 반복 {current_iteration}에서 작업 완료를 선언했습니다.")
                        break

            except Exception as processing_error:
                print(f"!!! 요청 처리 중 예외 발생 (반복 루프 내): {processing_error}")
                traceback.print_exc()
                final_llm_conclusion_text = f"[오류 발생: {processing_error}]"
                task_accomplished_by_llm = True  # 오류 발생 시 더 이상 진행하지 않음

            # --- 루프 종료 후 ---
            if not task_accomplished_by_llm:
                if current_iteration >= max_iterations:
                    print("최대 반복 횟수에 도달했습니다. LLM에게 요약을 요청합니다.")

                    # --- 최종 요약을 위한 추가 LLM 호출 ---
                    # 현재까지의 대화 내용에 요약을 요청하는 지침 추가
                    summarization_prompt = (
                        "You have now reached the maximum number of intermediate steps. "
                        "Please provide a final, conclusive answer to the user based on the conversation history so far. "
                        "Summarize what you have done and what the result is. "
                        "Do not call any more tools, just provide the final text response."
                        "그리고 한글로 답변해줘."
                    )
                    iteration_messages.append({"role": "user", "content": summarization_prompt})

                    try:
                        # 요약을 위한 마지막 LLM 호출 (도구 사용 비활성화)
                        final_summary_response = self.openai.chat.completions.create(
                            model=MODEL_NAME,  # 또는 self.MODEL_NAME
                            max_tokens=MAX_TOKENS,  # 또는 self.MAX_TOKENS
                            messages=iteration_messages,
                            tools=None,  # 더 이상 도구를 사용하지 못하도록 설정
                        )

                        final_llm_conclusion_text = final_summary_response.choices[0].message.content

                        if not final_llm_conclusion_text:
                            final_llm_conclusion_text = "[작업 요약 생성에 실패했습니다.]"

                    except Exception as summary_err:
                        print(f"!!! 최종 요약 생성 중 오류 발생: {summary_err}")
                        traceback.print_exc()
                        final_llm_conclusion_text = "[최대 반복 도달 후 요약 생성 중 오류가 발생했습니다.]"

                else:  # 다른 이유로 루프가 종료되었으나 명시적 완료가 아님 (이 경우는 거의 발생하지 않음)
                    final_llm_conclusion_text = "[작업이 명확히 완료되지 않고 종료됨]"

            if status_placeholder:
                status_placeholder.empty()
            if final_llm_conclusion_text and final_llm_conclusion_text.startswith(
                    "[") and final_llm_conclusion_text.endswith("]"):
                if last_tool_result_content:
                    print("LLM의 최종 결론이 없어 마지막 도구 실행 결과를 최종 답변으로 사용합니다.")
                    final_llm_conclusion_text = last_tool_result_content
            if TOOL_NAME in ("auto_tc_maker", "auto_test_scope_func"):
                final_llm_conclusion_text = result_content_for_llm

            print("\n--- 최종 반환될 내용 ---")
            print(f"  final_text content: {repr(final_llm_conclusion_text)}")
            print(f"  tool_status messages count: {len(accumulated_tool_status_messages)}")
            print("--- 최종 반환될 내용 끝 ---\n")

            return {
                "final_text": final_llm_conclusion_text,
                "tool_status": accumulated_tool_status_messages
            }


def main_dr_oh_page(key):
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    session_id = st.session_state.session_id

    st.markdown(
        """
        <h1 style='display: flex; align-items: center; gap: 10px;'>
            <img src='https://dszw1qtcnsa5e.cloudfront.net/community/20211023/5b80e92c-1b5d-4377-ab6c-cd0a73a75352/6e8b3aa55a5fbaa1a210a8b92bd559e7.jpg' alt='icon' width='80'/>
            오박사
        </h1>
        """,
        unsafe_allow_html=True
    )

    # 세션 상태 초기화 (채팅 기록만 유지)
    if 'messages' not in st.session_state:
        st.session_state.messages = [] # 채팅 기록 저장


    # --- 메인 채팅 인터페이스 ---
    st.header(f"💬 안녕하세요! 무엇이든 요청하세요!")
    print(f"\n--- 채팅 기록 표시 시작 ---{session_id}")
    from qa_mcp_server.slack_func.send_slack_msg import send_slack_message
    send_slack_message(f"`오박사 채팅 기록 시작 {session_id}`")

    print(f"st.session_state.messages 내용 (표시 직전,{session_id}):")
    try:
        pprint.pprint(st.session_state.get('messages', 'messages 키 없음'))
        send_slack_message(f"```오박사 채팅 기록 : {st.session_state.get('messages', 'messages 키 없음')},{session_id}```")
    except Exception as pp_err:
          print(f"(pprint 오류: {pp_err}), Raw: {st.session_state.get('messages', 'messages 키 없음')}")
          send_slack_message(f"```오박사 채팅 오류 {pp_err}: {st.session_state.get('messages', 'messages 키 없음')},{session_id}```")

    print(f"--- 채팅 기록 표시 전 로그 끝 {session_id} ---\n")
    send_slack_message(f"`오박사 채팅 기록 완료 {session_id}`")

    IMAGE_URL_PATTERN = re.compile(r'(https?://\S+\.(?:png|jpe?g|gif|webp|bmp|svg))', re.IGNORECASE)


    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "upload_counter" not in st.session_state:
        st.session_state.upload_counter = 0 # 카운터 초기화

    uploader_key = f"image_uploader_{st.session_state.upload_counter}" # 동적 키 생성

    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 0px;
            margin-top: 0px;
            color: #ffa500;
        }
        .custom-label + div {
            margin-top: 0px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # 사용자 정의 스타일로 라벨 출력
    st.markdown('<div class="custom-label"> 📎  이미지를 첨부하세요. 최대 10장까지만 처리합니다.</div>', unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        label="",  # 라벨 대신 위의 HTML 사용
        type=["png", "jpg", "jpeg", "gif", "webp", "bmp"],
        accept_multiple_files=True,
        key=uploader_key,
        help="최대 10장까지만 처리하며, 여러 파일을 동시에 업로드할 수 있습니다."
    )

    # API 키가 있어야만 입력 가능하도록 설정
    chat_input_disabled = not key

    if prompt := st.chat_input("메시지를 입력하세요...", disabled=chat_input_disabled, key="chat_input_main"):


        user_content_list = []
        image_paths = []  # 백엔드 전달용 이미지 변수

        # 업로드된 파일 처리
        MAX_FILES = 10

if __name__ == "__main__":
    main_dr_oh_page()


