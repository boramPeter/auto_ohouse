from typing import List, Dict, Any
from mcp import StdioServerParameters

'''
서버장비에서 실행할 용도의 MCP server 입니다. 여기에 TC 메이커 같은 MCP server가 지정될 예정입니다
'''

FLASK_SERVER_CONFIGURATIONS: List[Dict[str, Any]] = [
    {
        "id": "server1",
        "params": StdioServerParameters(
            command="/bin/bash",
            args=["-c", "cd /app && exec python3 -u -m qa_mcp_server.mcp_server_test_scope"],
            env={"PYTHONPATH": "/app"}
        )
    },
    {
        "id": "server2",
        "params": StdioServerParameters(
            command="/bin/bash",
            args=["-c", "cd /app && exec python3 -u -m qa_mcp_server.mcp_server_test_case_maker"],
            env={"PYTHONPATH": "/app"}
        )
    }

]