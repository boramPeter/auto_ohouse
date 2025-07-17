from mcp.server.fastmcp import FastMCP
from qa_mcp_server.qa_scope_module.scope_func import generate_test_scope
from qa_mcp_server.qa_scope_module.token_manager import print_status
from qa_mcp_server.qa_scope_module.read_content import read_google_content
from qa_mcp_server.figma.get_data_figma import run_multiple_analyses

import re
# MCP 서버 생성
mcp = FastMCP("TestScopeMaker", log_level="ERROR")

@mcp.tool()
def auto_test_scope_func(link: str = None, photo_paths: list = None, figma_name:list = None, figma_link: str = None) -> str:
    """test scope을 만드는 기능. 테스트범위를 도출하거나 산정할때 해당 함수가 실행되어야 한다.
    Args:
        link (str, optional): 테스트범위 대상이 될 Google Docs 문서의 전체 URL. 예: 'https://docs.google.com/document/d/...'
        photo_paths (list, optional): 사용자가 테스트범위 생성을 위해 함께 업로드한 이미지 파일들의 '로컬 파일 시스템 경로' 리스트.
                                   이 인수는 사용자가 명시적으로 이미지를 첨부했을 때만 사용되어야 하며,
                                   시스템(Streamlit 앱)이 전달하는 경로 리스트입니다.
                                   LLM은 이 경로를 직접 해석하는 것이 아니라, 이 경로가 존재한다는 사실과 함께
                                   테스트범위 생성 요청을 처리해야 합니다.
                                   예: ['/Users/peter.kim/ohs-AI-qa/uploaded_abc.png', '/Users/peter.kim/ohs-AI-qa/uploaded_xyz.png']
        figma_name (list, optional): figma의 layer이름입니다. "" 로 감싸진 텍스트이며 리스트로 처리합니다. 예: "주문 내역 - PC, 주문 내역 - MO"
        figma_link (str, optional): 테스트범위 도출의 기반이 될 figma 문서의 전체 URL. 예: 'https://www.figma.com/design/...'


    Returns:
        str: TC 생성 작업의 시작 또는 결과 메시지를 반환합니다.
    """
    if link is not None:
        doc_url = link
        doc_text = read_google_content(doc_url, sheet_name=None)
        print(doc_text)
        new_doc_content = doc_text
    else:
        new_doc_content = None
    derived_test_scope = None
    figma_msg = None
    if link is not None or photo_paths is not None:
        derived_test_scope = generate_test_scope(
            new_doc_text=new_doc_content,
            photo_path=photo_paths
        )
    if figma_link is not None:
        match = re.search(r'/design/([a-zA-Z0-9]+)', figma_link)
        file_key = match.group(1)
        print(file_key)
        figma_msg = run_multiple_analyses(figma_name, file_key, scope=True)

    msg = "\n=== 최종 도출된 테스트 범위 ===\n\n"
    if derived_test_scope:
        msg += derived_test_scope

    if figma_link:
        msg += figma_msg

    return msg


# 개인화된 인사 메시지 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """사용자에게 개인화된 인사 메시지를 제공"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()
