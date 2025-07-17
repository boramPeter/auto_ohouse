from typing import List, Dict, Any
from mcp import StdioServerParameters

'''
로컬에서 실행할 용도의 MCP server 입니다. 네이밍 규칙은 아래를 참고하세요

- 시작 문자: 반드시 영문자(a-z, A-Z) 또는 밑줄(_)로 시작해야함.
- 허용 문자: 영문자(a-z, A-Z), 숫자(0-9), 밑줄(_), 마침표(.), 또는 대시(-)만 사용가능.
- 최대 길이: 이름의 최대 길이는 64자.
'''

LOCAL_SERVER_CONFIGURATIONS: List[Dict[str, Any]] = [

    {
        "id": "playwright",
        "params": StdioServerParameters(
            command="npx", args=["@playwright/mcp@latest","--isolated"]
        )

    }

]