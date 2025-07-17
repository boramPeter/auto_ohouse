import os
import sys
from mcp.server.fastmcp import FastMCP
from mcp_automation.auto_locator_fix.find_case_method import find_and_append_runner

# MCP 서버 생성
mcp = FastMCP("AutoLocatorFixer", log_level="ERROR")

@mcp.tool()
def auto_locator_fix(platform: str, tc_id: str) -> str:
    """platform 은 안드로이드,android나 아이폰,ios로 들어오는데,platform에는 "android나" Or "ios"로 인식할것.  tc_id는 comm_platform00087 같은 형식으로 파라미터가 들어온다. UI자동화를 자동으로 보정해주는 기능"""
    find_and_append_runner(platform=platform,keyword=tc_id)
    if platform == "android":
        from mcp_automation.auto_ui_runner.android_AI_testrunner import main_aos
        main_aos()
        result = os.environ.get("ANDROID_AUTO_RESULT")
    else:
        from mcp_automation.auto_ui_runner.ios_AI_testrunner import main_ios
        main_ios()
        result = os.environ.get("IOS_AUTO_RESULT")
    msg = f"- {platform},{tc_id}의 자동화 보정이 완료되었습니다. \n\n- 결과 : {result} \n\n- 자세한 내용은 ai_fix_log 파일을 참고해주세요"
    return msg

# 개인화된 인사 메시지 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """사용자에게 개인화된 인사 메시지를 제공"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()
