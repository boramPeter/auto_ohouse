import threading,os,json
from qa_mcp_server.qa_scope_module.read_content import read_google_content
from qa_mcp_server.qa_scope_module.scope_func import generate_test_scope
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.chunk_test_scope import run_scope_extraction
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.embedding_func import embedded_test_scope
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.qdrant_search_case import search_from_qdrant
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.TC_make_chatbot import generate_testcase
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.make_testcase_func import write_to_spreadsheet,parse_markdown_table
from qa_mcp_server.figma.get_data_figma import run_multiple_analyses
import PIL.Image
from qa_mcp_server.slack_func.send_slack_msg import send_slack_message

# 1.PRD문서 읽기
def get_google_content(url: str) -> str:
    result = read_google_content(url)
    return result

# 1. 완료 : PRD문서를 읽어서 컨텍스트로 만들기
def docs_context(url:str = None, photo_path : list = None) -> str:
    if url is not None:
        result = read_google_content(url)
        prompt_for_prd = f"""
        안녕하세요, AI님. 지금부터 제가 제공하는 텍스트는 특정 프로젝트에 대한 전체 기획서입니다.
        이 기획서의 모든 내용을 주의 깊게 읽고, 세부 사항까지 완벽하게 분석 및 이해해주시기 바랍니다.
        특히 다음 사항들에 주목하여 내용을 파악해주십시오:
        - 프로젝트의 주요 목표 및 범위
        - 핵심 기능 및 각 기능의 상세 사양
        - 다양한 사용자 시나리오 및 예상되는 사용자 행동 흐름
        - 명시된 기능적/비기능적 요구사항
        - 시스템 제약 조건 또는 기술적 제한 사항
    
        이 기획서 내용을 바탕으로, 잠시 후 제가 상세한 테스트 케이스(TC) 작성을 요청드릴 예정입니다.
        제공되는 기획서 텍스트를 모두 검토하고 분석이 완료되면, "기획서 전체 내용에 대한 분석 및 이해가 완료되었습니다. 테스트 케이스 작성 준비가 되었습니다." 라고 명확히 응답해주십시오.
        만약 내용 이해에 필요한 질문이 있다면, 분석 완료 응답 전에 질문해주셔도 좋습니다.
    
        이제 아래에 프로젝트 기획서 전체 내용을 전달합니다.
    
        --- 기획서 시작 ---
        {result}
        --- 기획서 끝 ---
    
        위 기획서 내용을 면밀히 검토해주시고, 준비가 완료되면 알려주시기 바랍니다.
        """
    elif url is None and photo_path is not None:
        intro_text = """
        안녕하세요, AI님. 지금부터 제가 제공하는 이미지는 특정 프로젝트에 대한 오늘의집 서비스 화면 및 요구사항에 대한 내용 입니다.
        이 이미지의 모든 내용을 주의 깊게 보고, 세부 사항까지 완벽하게 분석 및 이해해주시기 바랍니다.
        특히 다음 사항들에 주목하여 내용을 파악해주십시오:
        - 프로젝트의 주요 목표 및 범위
        - 핵심 기능 및 각 기능의 상세 사양
        - 다양한 사용자 시나리오 및 예상되는 사용자 행동 흐름
        - 명시된 기능적/비기능적 요구사항
        - 시스템 제약 조건 또는 기술적 제한 사항
    
        이 이미지 내용을 바탕으로, 잠시 후 제가 상세한 테스트 케이스(TC) 작성을 요청드릴 예정입니다.
        제공되는 이미지를 모두 검토하고 분석이 완료되면, "이미지 내용에 대한 분석 및 이해가 완료되었습니다. 테스트 케이스 작성 준비가 되었습니다." 라고 명확히 응답해주십시오.
        만약 내용 이해에 필요한 질문이 있다면, 분석 완료 응답 전에 질문해주셔도 좋습니다.
    
        이제 아래에 이미지를 전달합니다.
        """

        # 프롬프트의 지침 부분 텍스트
        instructions = """
        위 이미지 내용을 면밀히 검토해주시고, 준비가 완료되면 알려주시기 바랍니다.
        """

        # contents 리스트 초기화 및 시작 텍스트 추가
        contents = [intro_text]

        # 이미지 경로 리스트를 순회하며 이미지와 마커 추가
        for image_path in photo_path:
            try:
                # 이미지 열기
                img = PIL.Image.open(image_path)

                # 마커와 이미지 추가
                contents.append("\n--- 이미지 시작 ---\n")
                contents.append(img)
                contents.append("\n--- 이미지 끝 ---\n")

            except Exception as e:
                return f"오류: 이미지를 여는 중 문제가 발생했습니다 ({image_path}): {e}"

        # 지침 텍스트 추가
        contents.append(instructions)
        prompt_for_prd = contents
    else:
        result = read_google_content(url)

        intro_text = """
                안녕하세요, AI님. 지금부터 제가 제공하는 텍스트와 이미지는 특정 프로젝트에 대한 오늘의집 서비스 화면 및 요구사항에 대한 내용 입니다.
                이 전체 텍스트와 이미지의 모든 내용을 주의 깊게 읽고 보고, 세부 사항까지 완벽하게 분석 및 이해해주시기 바랍니다.
                특히 다음 사항들에 주목하여 내용을 파악해주십시오:
                - 프로젝트의 주요 목표 및 범위
                - 핵심 기능 및 각 기능의 상세 사양
                - 다양한 사용자 시나리오 및 예상되는 사용자 행동 흐름
                - 명시된 기능적/비기능적 요구사항
                - 시스템 제약 조건 또는 기술적 제한 사항

                이 전체 텍스트와 이미지 내용을 바탕으로, 잠시 후 제가 상세한 테스트 케이스(TC) 작성을 요청드릴 예정입니다.
                제공되는 전체 텍스트, 이미지를 모두 검토하고 분석이 완료되면, "텍스트와 이미지 내용에 대한 분석 및 이해가 완료되었습니다. 테스트 케이스 작성 준비가 되었습니다." 라고 명확히 응답해주십시오.
                만약 내용 이해에 필요한 질문이 있다면, 분석 완료 응답 전에 질문해주셔도 좋습니다.

                이제 아래에 텍스트와 이미지를 전달합니다.
                """

        # 프롬프트의 지침 부분 텍스트
        instructions = """
        위 텍스트와 이미지 내용을 면밀히 검토해주시고, 준비가 완료되면 알려주시기 바랍니다.
        """

        # contents 리스트 초기화 및 시작 텍스트 추가
        contents = [intro_text]

        contents.append("\n--- 기획서 시작 ---\n")
        contents.append(result)
        contents.append("\n--- 기획서 끝 ---\n")

        # 이미지 경로 리스트를 순회하며 이미지와 마커 추가
        for image_path in photo_path:
            try:
                # 이미지 열기
                img = PIL.Image.open(image_path)

                # 마커와 이미지 추가
                contents.append("\n--- 이미지 시작 ---\n")
                contents.append(img)
                contents.append("\n--- 이미지 끝 ---\n")


            except Exception as e:
                return f"오류: 이미지를 여는 중 문제가 발생했습니다 ({image_path}): {e}"

        # 지침 텍스트 추가
        contents.append(instructions)
        prompt_for_prd = contents
    return prompt_for_prd

# 2. 3. test scope 읽기
def get_test_scope(text: str = None, photo:list = None) -> str:
    result = generate_test_scope(new_doc_text = text, photo_path = photo)
    return result

# 2. 완료 : scope을 읽어서 context로 만들기
def scope_context(scope: str) -> str:
    prompt = f"""안녕하세요. 지금부터 테스트 범위를 전달드립니다.

    이번 상호작용의 주요 목표는 당신이 아래 제공되는 테스트 범위를 **완벽하게 학습하고 이해**하는 것입니다. 
    실제 테스트 케이스를 작성하기에 앞서, 이 정보를 면밀히 검토하고 분석해주시길 바랍니다.

    **전달되는 테스트 범위:**
    ---
    {scope}
    ---

    **학습 및 이해를 위한 요청 사항:**
    1.  위에 제시된 테스트 범위 내용을 주의 깊게 읽고, 각 항목의 의미와 기능들 간의 상호 관계를 정확히 파악해주세요.
    2.  내용을 분석하는 과정에서 **모호하거나 불분명한 점, 이해를 위해 추가적인 설명이 필요한 부분, 또는 내용상 상충될 가능성이 있는 부분**이 있다면 주저하지 말고 저에게 질문해주십시오. 당신의 명확한 이해가 가장 중요합니다.
    3.  테스트 범위에 대한 학습 및 분석이 완료되었다고 판단되면, **당신이 이해한 내용을 바탕으로 핵심 기능, 주요 사용자 시나리오, 특별히 중요하다고 생각되는 제약 조건, 또는 기타 주요 사항들을 간략하게 요약**하여 저에게 다시 설명해주시겠습니까?
        이 요약 과정을 통해 저는 당신의 이해도를 확인할 수 있으며, 혹시 발생했을 수 있는 오해를 사전에 바로잡는 데 도움이 될 것입니다.

    이 학습 및 이해 확인 과정이 성공적으로 마무리된 후, 다음 단계에서 이 정보를 기반으로 구체적인 테스트 케이스 작성을 요청드릴 예정입니다.

    이제 위 테스트 범위에 대한 학습을 시작해주시고, 학습이 완료되면 완료되었다고 답변해주세요.
    """
    return prompt

# 3. 테스트 스코프 청킹 후 임베딩 -> 검색까지
def scope_chunk_and_embedded_retrieve(scope: str) -> str:
    scope_chunk = run_scope_extraction(scope)
    embedded_list = embedded_test_scope(scope_chunk)
    result = search_from_qdrant(embedded_list)
    return result

# 3. 완료: 검색된 내용들을 context로 만들기
def case_context(input_data) -> str:
    items_to_process = []
    if isinstance(input_data, list):
        if not input_data:
            print("오류: 빈 리스트가 제공되었습니다. 컨텍스트를 생성할 수 없습니다.")
            return "[컨텍스트 설정 오류: 빈 데이터 목록이 제공되었습니다.]"
        items_to_process = input_data
    elif isinstance(input_data, dict):
        items_to_process = [input_data]
    else:
        print(f"오류: 잘못된 데이터 타입입니다. 딕셔너리 또는 리스트를 기대했으나 {type(input_data)} 타입이 입력되었습니다.")
        return "[컨텍스트 설정 오류: 잘못된 데이터 타입입니다.]"

    all_formatted_scope_contexts = []
    valid_item_count = 0

    for index, item_dict in enumerate(items_to_process):
        if not isinstance(item_dict, dict):
            all_formatted_scope_contexts.append(
                f"\n--- [항목 {index + 1} 처리 오류]: 입력된 항목이 딕셔너리(dictionary) 형식이 아닙니다. 해당 항목 데이터: {str(item_dict)} ---\n"
            )
            continue

        valid_item_count += 1
        scope = item_dict.get('테스트 범위', f'지정되지 않은 테스트 범위 (항목 #{valid_item_count})')
        similar_cases_list = item_dict.get('유사 테스트 케이스', [])

        # 각 테스트 범위별 컨텍스트 문자열 조립 시작
        # 사용자의 요청 형식에 맞춤

        # --- [컨텍스트 블록 #{valid_item_count}] --- # 이 라인은 여러 블록 구분용으로 유지하거나, 단일 아이템 처리 시에는 제외 가능
        # 여기서는 사용자가 제시한 형식에만 집중하기 위해, 이 구분자는 최종 프롬프트에서만 사용되도록 하고
        # 개별 아이템 포맷팅에서는 이 구분자를 제외하고 순수하게 요청된 형식으로 만듭니다.

        scope_details_parts = [
            f"1.  **현재 집중해야 할 테스트 범위:**\n        \"{scope}\"",  # 실제 범위 내용은 8칸 들여쓰기
            f"\n2.  **위 테스트 범위와 관련된 참고용 유사 테스트 케이스 목록:**"
        ]

        if similar_cases_list:
            scope_details_parts.append("        다음은 참고용 유사 테스트 케이스들입니다:\n")  # 8칸 들여쓰기 및 줄바꿈
            for case_idx, case_info_dict in enumerate(similar_cases_list):
                label = f"    유사 사례 {case_idx + 1}:"  # 4칸 들여쓰기
                scope_details_parts.append(label)

                case_content_str = ""
                if isinstance(case_info_dict, dict):
                    case_content_str = case_info_dict.get('테스트케이스', '유사 테스트 케이스 내용이 비어있거나 키가 없습니다.')
                else:
                    case_content_str = f"(형식 오류 또는 직접 문자열 명시: {str(case_info_dict)})"

                # 각 줄을 4칸 들여쓰기
                indented_case_content_lines = [f"    {line}" for line in case_content_str.splitlines()]
                if not indented_case_content_lines:  # 내용이 비어있을 경우에도 최소한의 표시
                    scope_details_parts.append("    (내용 없음)")
                else:
                    scope_details_parts.extend(indented_case_content_lines)

                if case_idx < len(similar_cases_list) - 1:  # 마지막 유사 사례가 아니면 공백 라인 추가
                    scope_details_parts.append("")  # 한 줄 띄우기
        else:
            scope_details_parts.append("        (이 테스트 범위에 대해 제공된 참고 유사 테스트 케이스가 없습니다.)")  # 8칸 들여쓰기

        all_formatted_scope_contexts.append("\n".join(scope_details_parts))

    if valid_item_count == 0:
        return "[컨텍스트 설정 오류: 처리할 유효한 데이터 항목이 없습니다. 입력 형식을 확인해주세요.]"

    # 각 컨텍스트 블록 앞에 구분자 추가 (여러 아이템 처리 시)
    final_detail_blocks = []
    if len(items_to_process) > 1:  # 여러 아이템을 처리한 경우에만 블록 구분자 사용
        for i, block_content in enumerate(all_formatted_scope_contexts):
            final_detail_blocks.append(f"--- [컨텍스트 블록 #{i + 1}] ---\n{block_content}")
        final_scopes_details_str = "\n\n".join(final_detail_blocks)
    else:  # 단일 아이템 처리 시에는 블록 구분자 없이 바로 내용 표시
        final_scopes_details_str = all_formatted_scope_contexts[0]

    prompt = f"""
    [시스템 지침: {'다중 ' if valid_item_count > 1 else ''}컨텍스트 정보 학습]

    당신은 QA 전문가 AI 어시스턴트입니다. 지금부터 제가 제공하는 {'여러 ' if valid_item_count > 1 else ''}'테스트 범위' 각각과 그에 관련된 '참고용 유사 테스트 케이스' 정보를 학습하고 기억해주십시오.
    이 정보는 잠시 후 제가 요청할 '새로운 테스트 케이스 생성' 작업의 중요한 배경지식이 됩니다.
    {'각 테스트 범위 정보는 아래에 별도의 [컨텍스트 블록]으로 구분되어 제공됩니다.' if valid_item_count > 1 else ''}

    **학습 및 기억할 내용 ({f'총 {valid_item_count}개의 테스트 범위 컨텍스트' if valid_item_count > 1 else '다음 테스트 범위 컨텍스트'}):**

    {final_scopes_details_str}
    ---
    위 모든 내용을 충분히 숙지하고, 다음 저의 지시(특정 범위에 대한 테스트 케이스 생성 요청 또는 일반적인 생성 요청)가 있을 때 이 정보를 바탕으로 작업을 수행할 준비를 해주세요.
    이 메시지에 대해서는 "알겠습니다. {f'총 {valid_item_count}개의 테스트 범위 컨텍스트를 학습했습니다. ' if valid_item_count > 1 else '제공된 컨텍스트를 학습했습니다. '}준비되었습니다." 또는 유사한 간단한 확인 응답만 하고, 다른 추가 정보 생성이나 질문은 하지 마십시오.
    """
    print(f"context prompt: {prompt}")
    return prompt


# context들을 모아서 반환하는 함수
def create_context_helper(url: str = None, photo_path: list = None, figma_name: list = None, figma_file_key: str = None) -> tuple:
    send_slack_message(f"create_context_helper 시작 : {url,photo_path,figma_name,figma_file_key}")
    prd_text = None
    result_code = None

    if url is not None:
        prd_text = get_google_content(url)
        data_dict = json.loads(prd_text)
        response_code = data_dict['response_code']
        result_code = response_code

    scope = get_test_scope(prd_text, photo_path)
    print(scope)
    def task1_scope_context():
        return scope_context(scope)

    def task2_prd_context():
        return docs_context(prd_text, photo_path)

    def task3_scope_context():
        scope_dict = scope_chunk_and_embedded_retrieve(scope)
        return case_context(scope_dict)

    import queue
    t4_result_queue = queue.Queue()

    def task4_scope_context():
        result = run_multiple_analyses(figma_name, figma_file_key, scope=True,test_scope_context=True)
        t4_result_queue.put(result)

    t1 = t2 = t3 = t4 = None

    threads = []
    if url is not None or photo_path is not None:
        t1 = threading.Thread(target=task1_scope_context)
        t2 = threading.Thread(target=task2_prd_context)
        t3 = threading.Thread(target=task3_scope_context)
        threads.extend([t1, t2, t3])
    if figma_file_key is not None:
        t4 = threading.Thread(target=task4_scope_context)
        threads.append(t4)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # t4 결과값 추출
    t4_result = t4_result_queue.get() if figma_file_key is not None else None
    send_slack_message(f"create_context_helper 완료 : {t1, t2, t3, scope, prd_text, result_code if url is not None or photo_path is not None else None, t4_result}")

    return t1, t2, t3, scope, prd_text, result_code if url is not None or photo_path is not None else None, t4_result



# TC생성을 위한 프롬프트

def create_testcase_prompt(scope, prd_text:str = None, photo_path:list = None, desc:str = None):

    if prd_text is not None and photo_path is None:
        intro_text = """첨부된 문서를 분석하여, 이 문서에 명시된 요구사항들을 검증하기 위한 **상세하고 실행 가능한** 테스트 케이스(Test Case)를 자세하게 작성해주세요. 
        **요청사항:**
        
        """
        contents = [intro_text]

        prd_prompt = """1.  **첨부 문서**: 해당 문서를 참고해주세요. 해당 문서가 PRD 입니다.\n
        """
        contents.append(prd_prompt)
        contents.append("===PRD 시작===\n")
        contents.append(prd_text)
        contents.append("\n===PRD 종료===\n")

        origin_prompt_tc = f'''
            2.  **테스트 범위:** 
                PRD 문서의 내용과 아래의 테스트범위 및 요구사항들을 구체적으로 커버해주세요. 특히 앱의 경우 다양한 디바이스 해상도 및 OS 버전을 고려하여, 가능한 한 **다양하고 상세한 시나리오**(Positive, Negative, Edge cases 포함)를 만들어주세요.
                === 테스트범위 시작 ===
                {scope}
                === 테스트 범위 종료 ===

            3.  **출력 형식:** 
                테스트 케이스는 아래와 같은 컬럼을 포함하는 **Markdown 표(Table)** 형식으로 정리해주시면 좋겠습니다.
                
                * `Test Case ID`: 고유 식별자 (예: `PROJ-MYPAGE-001`). PRD 제목의 앞 4글자-화면분류-세 자리 숫자 형식으로 구성합니다.
                * `대상 기능/화면`: 테스트 대상이 되는 기능 또는 화면 명칭 (예: 마이페이지 > 프로필 편집). **가능한 한 구체적인 메뉴 경로**를 포함합니다.
                * `테스트 목적/시나리오`: **사용자 관점에서** 무엇을, 어떤 상황에서 검증하려는지 명확히 기술합니다. (예: 비로그인 사용자가 마이페이지 진입 시 로그인 페이지로 이동하는지 확인).
                * `전제 조건 (Pre-condition)`: 테스트 수행 전 **반드시 충족되어야 하는 명확한 시작 상태**를 기술합니다. (예: `사용자는 'test_user_01' 계정으로 로그인되어 있어야 함`, `장바구니에는 상품 A가 2개 담겨 있어야 함`, `푸시 알림 수신 동의 상태여야 함`). **구체적인 데이터 상태, 사용자 상태, 시스템 설정** 등을 명시합니다.
                * `테스트 경로/절차 (Test Steps)`: 검증을 위한 **구체적인 사용자 행동 단계**를 순차적으로 기술합니다. **어떤 화면에서 시작하여 어떤 경로(메뉴 이동, 버튼 클릭 등)를 통해 어떤 액션을 수행하는지** 명확하고 재현 가능하게 작성합니다.
                    1.  (예: 앱 실행)
                    2.  (예: 하단 탭 바에서 '마이페이지' 선택)
                    3.  (예: '프로필 편집' 버튼 클릭)
                    4.  (예: 닉네임 입력 필드에 'NewNick123' 입력)
                    5.  (예: '저장' 버튼 클릭)
                * `예상 결과 (Expected Result)`: 테스트 절차 수행 후 **시스템(화면, 데이터 등)이 보여야 하는 명확하고 검증 가능한 결과**를 기술합니다. (예: `'닉네임이 성공적으로 변경되었습니다.' 토스트 팝업 노출`, `마이페이지 화면의 닉네임이 'NewNick123'으로 변경되어 표시됨`).
                * `중요도 (Priority)`: 테스트 케이스의 중요도는 P0~P2로 표현합니다. (High = P0, Medium = P1, Low = P2).
                * `플랫폼/환경`: 관련 플랫폼 및 환경 (예: Web (Chrome), iOS (17.x), Android (13+), All, Server). **특정 환경에서만 발생 가능한 경우 명시**합니다.
                * `비고`: 추가적인 설명, PRD 연관 항목 (섹션 번호 등), 또는 **'상세 로직 정의 필요', '디자인 확인 필요'** 등 추가 확인이 필요한 사항을 명시합니다.

            4.  **상세 수준:**
                * QA 엔지니어가 이 문서만 보고도 **별도의 질문 없이 테스트를 수행할 수 있을 정도로 명확하고 상세하게** 작성합니다.
                * 특히 **`전제 조건`과 `테스트 경로/절차`는 누가 수행하더라도 동일한 결과를 얻을 수 있도록 구체적**이어야 합니다.
                * PRD에 명시되지 않아 구체화가 어려운 부분은 **`비고`란에 명확히** 표시하여 추후 논의가 가능하도록 합니다.

            5.  **테스트케이스 작성 시 지침:**
                * **학습 활용:** 기존 대화에서 학습한 프로젝트 기획서, 테스트 범위, 유사 케이스 작성 경험을 **최대한 활용**하여 TC를 작성합니다.
                * **경로 및 조건 중심:** 모든 테스트 케이스 작성 시, **'어떤 상태에서(Pre-condition)'** 시작하여 **'어떤 경로를 통해(Test Steps)'** 검증하는지를 **가장 중요하게** 고려합니다.
                * **다각적 접근:** 기능의 **정상 동작(Positive)** 뿐만 아니라, **예외 상황(Negative)**, **경계값/극한 상황(Edge cases)**, **사용성/UI/UX 측면**까지 고려하여 폭넓은 케이스를 도출합니다.
                * **데이터 고려:** 테스트에 필요한 **특정 데이터**(예: 긴 텍스트, 특수 문자, 빈 값, 특정 형식의 데이터)를 `테스트 절차` 또는 `전제 조건`에 명시합니다.
                * **사용자 역할:** 여러 사용자 역할(예: 일반 사용자, 관리자, 신규 사용자)이 있다면, **역할별 시나리오**를 고려합니다.
                * **일관성:** `Test Case ID` 네이밍 규칙 및 표 형식을 일관되게 유지합니다.
                * **최종 결과물:** 작성된 모든 케이스들을 **Markdown이 적용된 하나의 표**로 만들어 한글로 답변합니다. 
        '''
        contents.append(origin_prompt_tc)
        prompt_for_tc = contents

    elif photo_path is not None and prd_text is None:
        intro_text = """첨부된 이미지를 분석하여, 이 이미지에 명시된 요구사항 및 오늘의집 서비스를 검증하기 위한 **상세하고 실행 가능한** 테스트 케이스(Test Case)를 자세하게 작성해주세요.
                **요청사항:**
                
                """
        contents = [intro_text]
        img_prompt = f"""1. **첨부 이미지**: 해당 이미지들을 참고해주세요. 해당 이미지가 요구사항 이미지와 오늘의집 서비스 화면 입니다. 만약 첨부된 이미지가 서비스 화면이 아닌 텍스트로 이루어져 있다면 텍스트를 꼼꼼하게 확인하세요.
                """
        contents.append(img_prompt)
        for image_path in photo_path:
            try:
                img = PIL.Image.open(image_path)
                contents.append("===새 이미지 시작===\n")
                contents.append(img)
                contents.append("\n===새 이미지 시작===\n")

            except Exception as e:
                return f"오류: 이미지를 여는 중 문제가 발생했습니다 ({image_path}): {e}"

        origin_prompt_tc = f'''
                    2.  **테스트 범위:**
                        이미지 내에 오늘의집 서비스화면, 그리고 텍스트 내용과 아래의 테스트범위 및 요구사항들을 구체적으로 커버해주세요. 특히 앱의 경우 다양한 디바이스 해상도 및 OS 버전을 고려하여, 가능한 한 **다양하고 상세한 시나리오**(Positive, Negative, Edge cases 포함)를 만들어주세요.
                        === 테스트범위 시작 ===
                        {scope}
                        === 테스트 범위 종료 ===

                    3.  **출력 형식:** 
                        테스트 케이스는 아래와 같은 컬럼을 포함하는 **Markdown 표(Table)** 형식으로 정리해주시면 좋겠습니다.
                        * `Test Case ID`: 고유 식별자 (예: `PROJ-MYPAGE-001`). PRD 제목의 앞 4글자-화면분류-세 자리 숫자 형식으로 구성합니다.
                        * `대상 기능/화면`: 테스트 대상이 되는 기능 또는 화면 명칭 (예: 마이페이지 > 프로필 편집). **가능한 한 구체적인 메뉴 경로**를 포함합니다.
                        * `테스트 목적/시나리오`: **사용자 관점에서** 무엇을, 어떤 상황에서 검증하려는지 명확히 기술합니다. (예: 비로그인 사용자가 마이페이지 진입 시 로그인 페이지로 이동하는지 확인).
                        * `전제 조건 (Pre-condition)`: 테스트 수행 전 **반드시 충족되어야 하는 명확한 시작 상태**를 기술합니다. (예: `사용자는 'test_user_01' 계정으로 로그인되어 있어야 함`, `장바구니에는 상품 A가 2개 담겨 있어야 함`, `푸시 알림 수신 동의 상태여야 함`). **구체적인 데이터 상태, 사용자 상태, 시스템 설정** 등을 명시합니다.
                        * `테스트 경로/절차 (Test Steps)`: 검증을 위한 **구체적인 사용자 행동 단계**를 순차적으로 기술합니다. **어떤 화면에서 시작하여 어떤 경로(메뉴 이동, 버튼 클릭 등)를 통해 어떤 액션을 수행하는지** 명확하고 재현 가능하게 작성합니다.
                            1.  (예: 앱 실행)
                            2.  (예: 하단 탭 바에서 '마이페이지' 선택)
                            3.  (예: '프로필 편집' 버튼 클릭)
                            4.  (예: 닉네임 입력 필드에 'NewNick123' 입력)
                            5.  (예: '저장' 버튼 클릭)
                        * `예상 결과 (Expected Result)`: 테스트 절차 수행 후 **시스템(화면, 데이터 등)이 보여야 하는 명확하고 검증 가능한 결과**를 기술합니다. (예: `'닉네임이 성공적으로 변경되었습니다.' 토스트 팝업 노출`, `마이페이지 화면의 닉네임이 'NewNick123'으로 변경되어 표시됨`).
                        * `중요도 (Priority)`: 테스트 케이스의 중요도는 P0~P2로 표현합니다. (High = P0, Medium = P1, Low = P2). 
                        * `플랫폼/환경`: 관련 플랫폼 및 환경 (예: Web (Chrome), iOS (17.x), Android (13+), All, Server). **특정 환경에서만 발생 가능한 경우 명시**합니다.
                        * `비고`: 추가적인 설명, PRD 연관 항목 (섹션 번호 등), 또는 **'상세 로직 정의 필요', '디자인 확인 필요'** 등 추가 확인이 필요한 사항을 명시합니다.

                    4.  **상세 수준:**
                        * QA 엔지니어가 이 문서만 보고도 **별도의 질문 없이 테스트를 수행할 수 있을 정도로 명확하고 상세하게** 작성합니다.
                        * 특히 **`전제 조건`과 `테스트 경로/절차`는 누가 수행하더라도 동일한 결과를 얻을 수 있도록 구체적**이어야 합니다.
                        * PRD에 명시되지 않아 구체화가 어려운 부분은 **`비고`란에 명확히** 표시하여 추후 논의가 가능하도록 합니다.

                    5.  **테스트케이스 작성 시 지침:**
                        * **학습 활용:** 기존 대화에서 학습한 프로젝트 기획서, 테스트 범위, 유사 케이스 작성 경험을 **최대한 활용**하여 TC를 작성합니다.
                        * **경로 및 조건 중심:** 모든 테스트 케이스 작성 시, **'어떤 상태에서(Pre-condition)'** 시작하여 **'어떤 경로를 통해(Test Steps)'** 검증하는지를 **가장 중요하게** 고려합니다.
                        * **다각적 접근:** 기능의 **정상 동작(Positive)** 뿐만 아니라, **예외 상황(Negative)**, **경계값/극한 상황(Edge cases)**, **사용성/UI/UX 측면**까지 고려하여 폭넓은 케이스를 도출합니다.
                        * **데이터 고려:** 테스트에 필요한 **특정 데이터**(예: 긴 텍스트, 특수 문자, 빈 값, 특정 형식의 데이터)를 `테스트 절차` 또는 `전제 조건`에 명시합니다.
                        * **사용자 역할:** 여러 사용자 역할(예: 일반 사용자, 관리자, 신규 사용자)이 있다면, **역할별 시나리오**를 고려합니다.
                        * **일관성:** `Test Case ID` 네이밍 규칙 및 표 형식을 일관되게 유지합니다.
                        * **최종 결과물:** 작성된 모든 케이스들을 **Markdown이 적용된 하나의 표**로 만들어 한글로 답변합니다. 
                '''
        contents.append(origin_prompt_tc)
        prompt_for_tc = contents
    elif photo_path is not None and prd_text is not None:
        intro_text = """첨부된 문서와 이미지를 분석하여, 이 문서와 이미지에 명시된 요구사항 및 오늘의집 서비스를 검증하기 위한 **상세하고 실행 가능한** 테스트 케이스(Test Case)를 자세하게 작성해주세요.
                        **요청사항:**

                        """
        contents = [intro_text]
        prd_prompt = """1.  **첨부 문서**: 해당 문서를 참고해주세요. 해당 문서가 PRD 입니다.
        """
        img_prompt = f"""2. **첨부 이미지**: 해당 이미지들을 참고해주세요. 해당 이미지가 요구사항 이미지와 오늘의집 서비스 화면 입니다.
                        """
        contents.append(prd_prompt)
        contents.append("===PRD 시작===\n")
        contents.append(prd_text)
        contents.append("\n===PRD 종료===\n")

        contents.append(img_prompt)
        for image_path in photo_path:
            try:
                img = PIL.Image.open(image_path)
                contents.append("===새 이미지 시작===\n")
                contents.append(img)
                contents.append("\n===새 이미지 시작===\n")

            except Exception as e:
                return f"오류: 이미지를 여는 중 문제가 발생했습니다 ({image_path}): {e}"


        origin_prompt_tc = f'''
                            3.  **테스트 범위:** 
                                PRD문서, 이미지 내에 표현된 내용과 아래의 테스트범위 및 요구사항들을 구체적으로 커버해주세요. 특히 앱의 경우 다양한 디바이스 해상도 및 OS 버전을 고려하여, 가능한 한 **다양하고 상세한 시나리오**(Positive, Negative, Edge cases 포함)를 만들어주세요. 만약 첨부된 이미지가 서비스 화면이 아닌 텍스트로 이루어져 있다면 텍스트를 꼼꼼하게 확인하세요.
                                === 테스트범위 시작 ===
                                {scope}
                                === 테스트 범위 종료 ===

                            4.  **출력 형식:** 
                                테스트 케이스는 아래와 같은 컬럼을 포함하는 **Markdown 표(Table)** 형식으로 정리해주시면 좋겠습니다.
                                * `Test Case ID`: 고유 식별자 (예: `PROJ-MYPAGE-001`). PRD 제목의 앞 4글자-화면분류-세 자리 숫자 형식으로 구성합니다.
                                * `대상 기능/화면`: 테스트 대상이 되는 기능 또는 화면 명칭 (예: 마이페이지 > 프로필 편집). **가능한 한 구체적인 메뉴 경로**를 포함합니다.
                                * `테스트 목적/시나리오`: **사용자 관점에서** 무엇을, 어떤 상황에서 검증하려는지 명확히 기술합니다. (예: 비로그인 사용자가 마이페이지 진입 시 로그인 페이지로 이동하는지 확인).
                                * `전제 조건 (Pre-condition)`: 테스트 수행 전 **반드시 충족되어야 하는 명확한 시작 상태**를 기술합니다. (예: `사용자는 'test_user_01' 계정으로 로그인되어 있어야 함`, `장바구니에는 상품 A가 2개 담겨 있어야 함`, `푸시 알림 수신 동의 상태여야 함`). **구체적인 데이터 상태, 사용자 상태, 시스템 설정** 등을 명시합니다.
                                * `테스트 경로/절차 (Test Steps)`: 검증을 위한 **구체적인 사용자 행동 단계**를 순차적으로 기술합니다. **어떤 화면에서 시작하여 어떤 경로(메뉴 이동, 버튼 클릭 등)를 통해 어떤 액션을 수행하는지** 명확하고 재현 가능하게 작성합니다.
                                    1.  (예: 앱 실행)
                                    2.  (예: 하단 탭 바에서 '마이페이지' 선택)
                                    3.  (예: '프로필 편집' 버튼 클릭)
                                    4.  (예: 닉네임 입력 필드에 'NewNick123' 입력)
                                    5.  (예: '저장' 버튼 클릭)
                                * `예상 결과 (Expected Result)`: 테스트 절차 수행 후 **시스템(화면, 데이터 등)이 보여야 하는 명확하고 검증 가능한 결과**를 기술합니다. (예: `'닉네임이 성공적으로 변경되었습니다.' 토스트 팝업 노출`, `마이페이지 화면의 닉네임이 'NewNick123'으로 변경되어 표시됨`).
                                * `중요도 (Priority)`: 테스트 케이스의 중요도는 P0~P2로 표현합니다. (High = P0, Medium = P1, Low = P2). 
                                * `플랫폼/환경`: 관련 플랫폼 및 환경 (예: Web (Chrome), iOS (17.x), Android (13+), All, Server). **특정 환경에서만 발생 가능한 경우 명시**합니다.
                                * `비고`: 추가적인 설명, PRD 연관 항목 (섹션 번호 등), 또는 **'상세 로직 정의 필요', '디자인 확인 필요'** 등 추가 확인이 필요한 사항을 명시합니다.

                            5.  **상세 수준:**
                                * QA 엔지니어가 이 문서만 보고도 **별도의 질문 없이 테스트를 수행할 수 있을 정도로 명확하고 상세하게** 작성합니다.
                                * 특히 **`전제 조건`과 `테스트 경로/절차`는 누가 수행하더라도 동일한 결과를 얻을 수 있도록 구체적**이어야 합니다.
                                * PRD에 명시되지 않아 구체화가 어려운 부분은 **`비고`란에 명확히** 표시하여 추후 논의가 가능하도록 합니다.

                            6.  **테스트케이스 작성 시 지침:**
                                * **학습 활용:** 기존 대화에서 학습한 프로젝트 기획서, 테스트 범위, 유사 케이스 작성 경험을 **최대한 활용**하여 TC를 작성합니다.
                                * **경로 및 조건 중심:** 모든 테스트 케이스 작성 시, **'어떤 상태에서(Pre-condition)'** 시작하여 **'어떤 경로를 통해(Test Steps)'** 검증하는지를 **가장 중요하게** 고려합니다.
                                * **다각적 접근:** 기능의 **정상 동작(Positive)** 뿐만 아니라, **예외 상황(Negative)**, **경계값/극한 상황(Edge cases)**, **사용성/UI/UX 측면**까지 고려하여 폭넓은 케이스를 도출합니다.
                                * **데이터 고려:** 테스트에 필요한 **특정 데이터**(예: 긴 텍스트, 특수 문자, 빈 값, 특정 형식의 데이터)를 `테스트 절차` 또는 `전제 조건`에 명시합니다.
                                * **사용자 역할:** 여러 사용자 역할(예: 일반 사용자, 관리자, 신규 사용자)이 있다면, **역할별 시나리오**를 고려합니다.
                                * **일관성:** `Test Case ID` 네이밍 규칙 및 표 형식을 일관되게 유지합니다.
                                * **최종 결과물:** 작성된 모든 케이스들을 **Markdown이 적용된 하나의 표**로 만들어 한글로 답변합니다. 
                        '''
        contents.append(origin_prompt_tc)
        prompt_for_tc = contents
    else:
        return None
    if desc is not None:
        add_prompt = '''
        위에 프롬프트에서 해당 내용을 추가합니다. 테스트케이스 생성시에 아래 내용을 참고해주세요. **위의 프롬프트와 아래 프롬프트의 지시사힝이 겹친다면**, 아래의 프롬프트로 수행해주세요.
        
        === 지시사항 추가 ===
        '''
        prompt_for_tc.append(add_prompt)
        prompt_for_tc.append(desc)
    return prompt_for_tc


# TC생성시 참고할 context 함수
def run_testcase_maker(url):
    scope_context,prd_context,case_context,scope,prd_text = create_context_helper(url)
    tc_prompt = create_testcase_prompt(scope,prd_text)
    result_msg = generate_testcase(scope_context,prd_context,case_context,tc_prompt)
    parsed_table = parse_markdown_table(result_msg)
    result_msg += write_to_spreadsheet(parsed_table)
    return result_msg

# t = run_testcase_maker("https://docs.google.com/document/d/1Vt7JNR_1-nrWb0mv9qm08-pusAppMKb7G7-LpC7KFO8/edit?tab=t.721ze2s69fk2")
# print(t)
# text = '''
# 네, 새로운 문서를 꼼꼼히 읽고 학습한 패턴에 따라 테스트 범위를 도출했습니다.
#
# 테스트 범위
#
# 1. 광고 호출 및 응답 기본 검증 * [공통] 신규 인벤토리 코드(cart_bottom_stylingshot, order_result_stylingshot, myshopping_stylingshot)를 사용하여 SSP(/v1/ads)에 광고 요청 정상 동작 확인. * [공통] 광고 요청 시 pageId (ohslog 기준) 파라미터 정상 전달 확인. * [공통] SSP 응답으로 최대 20개의 광고 수신 및 노출 확인. * [공통] SSP 응답 광고 개수가 2개 미만일 경우, 클라이언트에서 해당 광고 모듈 미노출 처리 확인 (SSP에서 제어하므로, 클라이언트는 응답없음/부족 시 정상 처리하는지 확인). * [공통] 광고 응답으로 내려온 scrap 상태(스크랩/미스크랩)가 UI에 정확히 반영되는지 확인.
#
# 2. 스타일링샷 광고 모듈 UI 및 기능 검증 (2-Grid 형태) * 2.1. 공통 UI 요소 검증 * 모듈 상단 타이틀 "이런 연출이 가능한 상품은 어떠세요?" 문구 노출 확인 (클릭 불가). * 각 광고 아이템별 'AD 뱃지' 노출 및 클릭 시 광고 안내 툴팁 노출 확인 (광고 공통 사양). * 스타일링샷 이미지 1:1.07 비율 크롭 및 노출 확인 (썸네일 사이즈 42px 조정 반영). * 이미지 내 상품 태그가 크롭된 이미지 영역 내에 있을 경우에만 노출 확인. * 상품 정보 영역 (상품 썸네일, 상품명, 가격, 리뷰 평점, 리뷰 수/스크랩 수) 정상 노출 확인. * 상품명, 가격, 스크랩 수 텍스트 오버플로우 시 말줄임표(...) 처리 및 줄바꿈 없음 확인. * 리뷰 수 없을 시 스크랩 수 노출 로직 확인. * 2.2. 광고 아이템 정렬 및 스크롤 검증 * 광고 아이템은 SSP 응답 순서대로 좌에서 우로, 위에서 아래로 정렬되어 노출 확인. * 광고 아이템이 화면 너비를 초과할 경우, 2-Grid 모듈 전체의 수평 스크롤 기능 정상 동작 확인. * 2.3. 클릭 동작 검증 * 스타일링샷 이미지 전체 영역 (이미지 내 상품 태그 포함) 클릭 시 해당 상품의 PDP로 이동 확인. * 상품 정보 영역 (썸네일, 상품명, 가격, 평점, 리뷰/스크랩수 텍스트 영역) 클릭 시 해당 상품의 PDP로 이동 확인. * 스크랩 아이콘 클릭 시: * 미스크랩 상태에서 클릭 시 스크랩 처리 및 아이콘 상태 변경 확인. * 스크랩 상태에서 클릭 시 언스크랩 처리 및 아이콘 상태 변경 확인.
#
# 3. 지면별 광고 모듈 레이아웃 및 순서 검증 * 3.1. 장바구니 리스트 하단 (cart_bottom_stylingshot) * XPC 그룹 A (광고 미노출): 상품광고 > 추천상품 순서로 노출 확인. * XPC 그룹 B (광고 노출): 스타일링샷 광고 (신규) > 상품광고 > 추천상품 순서로 노출 확인. (문서에는 상품광고 > 추천상품 > 스타일링샷광고 로 되어있으나, 일반적으로 신규 광고를 먼저 테스트하므로 스타일링샷 광고 (신규) > 상품광고 > 추천상품 순서로 가정하여 기재. 실제 문서 내용에 따른다면 상품광고 > 추천상품 > 스타일링샷 광고 순서 확인) * 문서 정정: 문서 XPC 테이블 기준 "상품광고 > 추천상품 > 스타일링샷광고" 순서 확인. * 3.2. 주문완료 하단 (order_result_stylingshot) * XPC 그룹 A (광고 미노출): 상품광고만 노출 확인. * XPC 그룹 B (광고 노출): 스타일링샷 광고 (신규) > 상품광고 순서로 노출 확인. (문서에는 상품광고 > 스타일링샷광고 로 되어있으므로 해당 순서 확인) * 문서 정정: 문서 XPC 테이블 기준 "상품광고 > 스타일링샷광고" 순서 확인. * 3.3. 마이쇼핑 하단 (myshopping_stylingshot) * XPC 그룹 A (광고 미노출): 상품광고만 노출 확인. * XPC 그룹 B (광고 노출): 스타일링샷 광고 (신규) > 상품광고 순서로 노출 확인. (문서에는 상품광고 > 스타일링샷광고 로 되어있으므로 해당 순서 확인) * 문서 정정: 문서 XPC 테이블 기준 "상품광고 > 스타일링샷광고" 순서 확인.
#
# 4. 데이터 로깅 검증 * 각 지면(장바구니, 주문완료, 마이쇼핑)별 신규 스타일링샷 광고 모듈에 대해 다음 로그 발생 조건 및 파라미터 정확성 확인: * impression (ohs-log: 1773, 1778, 1783 / ads-log: impression): 1px 이상 노출 시. * viewable_impression (ohs-log: 1774, 1779, 1784 / ads-log: viewable_impression): 50% 이상 1초 연속 노출 시 (FE 바 높이 고려한 viewable impression 추후 개선 예정 인지). * card_click (ohs-log: 1775, 1780, 1785 (data.click_area로 구분) / ads-log: card_click): 스타일링샷 (이미지, 이미지 내 태그) 클릭 시. * product_click (ads-log: product_click): 상품 정보 영역 클릭 시. * scrap_click (ohs-log: 1776, 1781, 1786 / ads-log: scrap_click): 스크랩 아이콘 클릭하여 스크랩 시. * unscrap (ohs-log: 1777, 1782, 1787 / ads-log: 호출 안함): 스크랩 아이콘 클릭하여 언스크랩 시. * 로그 전송 시 각 지면에 해당하는 pageId가 정확히 포함되는지 확인.
#
# 5. XPC 실험 연동 검증 * 각 지면별 XPC 설정(1467, 1468, 1469)에 따라 그룹 A(광고 미노출)와 그룹 B(광고 노출) 분기 처리 및 UI 노출 정상 동작 확인.
#
# 6. (부가항목) 상품 광고와의 중복 노출 확인 * 스타일링샷 광고에 노출된 상품이 동일 페이지 내 다른 상품 광고 영역(e.g., 상품광고)에도 중복으로 노출되는지 여부 확인 (정책상 허용되나 현상 파악 목적).
#
# 최종 검토:
#
# 문서 내용 기반 누락 여부:
# 클라이언트-SSP 연동: Inventory code 사용, 최대/최소 응답 개수 처리, API 엔드포인트 및 pageId 전달. → 포함됨.
# XPC 연동: SSP 제어, 클라이언트는 응답대로 노출. → 포함됨.
# 디자인 요구사항: 2-grid 형태, 필수 노출 요소(AD뱃지, 이미지, 상품정보 등), 타이틀, 이미지 비율, 클릭 영역 및 동작(PDP 이동, 스크랩/언스크랩). → 포함됨.
# 지면별 노출 위치 및 순서 (XPC 그룹별). → 정정하여 포함됨.
# 데이터 요건: ads_log, ohs_log 이벤트 종류 및 pageId. → 포함됨.
# FE 개발 참고사항 (vimp 정책, 이미지 크롭 및 태그 위치 계산 등)은 직접적인 테스트 범위보다는 구현 가이드로 보이나, 결과적으로 vimp 로그는 검증 범위에 포함됨.
# "상품인벤토리와 중복광고 노출" 관련 내용 → 부가항목으로 포함됨.
# 중복 및 간결성: 최대한 중복을 피하고 주요 기능 중심으로 정리하려 했으며, 각 항목은 구체적인 검증 대상을 명시했습니다.
# 패턴 적용: 이전 예시들처럼 문서의 주요 기능/구성요셔(광고 호출, UI, 데이터, XPC)를 파악하고, 이를 검증하기 위한 구체적인 테스트 항목을 정의하는 패턴을 적용했습니다.
# 위와 같이 테스트 범위를 도출했습니다. 문서 내용이 방대하여 일부 해석에 따라 테스트 항목의 상세 수준이 달라질 수 있으나, 주요 기능은 대부분 커버되었다고 판단됩니다.
#
#
# '''
# result = scope_chunk_and_embedded_retrieve(text)
# p = create_testcase_prompt(scope=text,prd_text=None,photo_path=["/Users/peter.kim/Desktop/test.png"])
# print(p)

