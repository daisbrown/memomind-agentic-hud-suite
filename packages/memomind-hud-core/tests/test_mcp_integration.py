"""Exercise actual MCP stdio initialization, discovery and tool calls."""
import asyncio
import json
from pathlib import Path
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[3]


def test_gate_stdio():
    async def run():
        params = StdioServerParameters(command=sys.executable, args=[str(ROOT / 'projects/01-claude-hud-gate/mcp_server.py')])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                assert 'request_hud_approval' in [t.name for t in tools.tools]
                result = await session.call_tool('request_hud_approval', {'command':'DROP TABLE users', 'target_files':[], 'diff_summary':'Drop table'})
                assert not result.isError
                assert json.loads(result.content[0].text)['approved'] is False
                assert json.loads(result.content[0].text)['risk'] == 'HIGH'
    asyncio.run(run())


def test_field_ops_stdio():
    async def run():
        params = StdioServerParameters(command=sys.executable, args=[str(ROOT / 'projects/04-voice-mcp-field-ops/mcp_server.py')])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool('get_pinout', {'name':'OBD-II'})
                assert not result.isError
                assert json.loads(result.content[0].text)['pins']['4'] == 'chassis ground'
    asyncio.run(run())
