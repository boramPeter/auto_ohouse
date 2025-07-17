import time,os,re
from mcp.server.fastmcp import FastMCP
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.TC_make_chatbot import generate_testcase
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.TC_maker_runner import create_testcase_prompt, \
    create_context_helper
from qa_mcp_server.TC_auto_maker_module.TC_auto_maker.make_testcase_func import write_to_spreadsheet, \
    parse_markdown_table
from qa_mcp_server.msg_manager import save_to_json,delete_top_key
from qa_mcp_server.figma.get_data_figma import run_multiple_analyses
from concurrent.futures import ThreadPoolExecutor, as_completed
from qa_mcp_server.slack_func.send_slack_msg import send_slack_message

# MCP 서버 생성
mcp = FastMCP("AutoTestCaseMaker", log_level="ERROR")


@mcp.tool()
def auto_tc_maker(link: str = None, photo_paths: list = None, desc: str = None, figma_name:list = None, figma_link: str = None) -> str:
    '''
    mcp 기본 구조는 mcp_server_test_scope으로 확인 되기에 로직 제거.
    '''

# 개인화된 인사 메시지 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """사용자에게 개인화된 인사 메시지를 제공"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()
