

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    # 1. Point to your server script
    server_params = StdioServerParameters(
        command="python",
        args=["module-1/mcp_ak/server.py"], # Path to your server
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 2. Initialize the connection
            await session.initialize()

            # 3. List available tools (The "Discovery" phase)
            tools = await session.list_tools()
            print(f"Discovered Tools: {[t.name for t in tools.tools]}")

            # 4. Call a tool (The "Request" phase)
            result = await session.call_tool("graph_lookup", arguments={"entity_query": "Alice"})
            print(f"Result from Server: {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(run_client())













##########################################################################################
# import asyncio
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage

# # 1. Point to your server file
# server_params = StdioServerParameters(
#     command="python",
#     args=["server.py"], 
# )

# async def run_mcp_client():
#     async with stdio_client(server_params) as (read, write):
#         async with ClientSession(read, write) as session:
#             # Initialize the connection
#             await session.initialize()
            
#             # 2. List available tools from the server
#             tools_result = await session.list_tools()
#             print(f"Server shared these tools: {[t.name for t in tools_result.tools]}")

#             # 3. Use Gemini to decide which tool to call
#             llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
            
#             # Mapping MCP tools to LLM-compatible format
#             # (In production, you'd use a helper to convert these automatically)
#             query = "How much money does Arthur have in the Sterling vault?"
            
#             # For this demo, we'll simulate the tool execution via the session
#             # result = await session.call_tool("get_account_balance", {"member_name": "Arthur"})
#             # print(f"Result from MCP Server: {result.content[0].text}")

# if __name__ == "__main__":
#     asyncio.run(run_mcp_client())