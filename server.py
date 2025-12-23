from mcp.server import MCPServer

server = MCPServer(
    name="demo-mcp-server",
    description="Test MCP server for security scanning"
)

@server.tool()
def get_user_data(user_id: str):
    return {
        "user_id": user_id,
        "role": "admin",
        "token": "hardcoded-secret"
    }

server.run()

