"""Read-only risk analysis MCP server. It cannot approve or execute commands."""
from mcp.server.fastmcp import FastMCP
from memomind_core import HUDFormatter
from risk_analyzer import classify

mcp = FastMCP('HUD Gate')

@mcp.tool()
def request_hud_approval(command: str, target_files: list[str], diff_summary: str) -> dict:
    """Create a review card. Approval is unavailable until a trusted input is connected."""
    risk = classify(command, target_files)
    frame = HUDFormatter().format([f'[GATE: {risk}]', diff_summary, 'APPROVAL UNAVAILABLE'])
    return {'risk': risk, 'frame': list(frame.lines), 'approved': False, 'status': 'unavailable'}

if __name__ == '__main__': mcp.run(transport='stdio')
