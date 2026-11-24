"""Local stdio MCP tools for reference lookups and read-only Docker status."""
from mcp.server.fastmcp import FastMCP
from mcp_providers.pinout_lookup import lookup
from mcp_providers.docker_health import list_containers

mcp = FastMCP('Field Ops')

@mcp.tool()
def get_pinout(name: str) -> dict:
    """Look up reference pins; confirm against device documentation before wiring."""
    try: return {'pins': lookup(name), 'note': 'Verify against device documentation.'}
    except KeyError: return {'error': 'Unknown pinout'}

@mcp.tool()
def docker_containers() -> list[dict]:
    """List containers from the local Docker daemon without modifying them."""
    return list_containers()

if __name__ == '__main__': mcp.run(transport='stdio')
