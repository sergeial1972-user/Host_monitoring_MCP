#imports
import requests
from http import HTTPStatus
from mcp.server.fastmcp import FastMCP
import asyncio
#
from dotenv import load_dotenv
import os

#dotenv
load_dotenv()

mcp = FastMCP("HostMonitoring", host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))

@mcp.tool()
def check_host(host: str) -> dict:
    """Check HTTP status of a host.

    Args:
        host: Full URL (https://example.com)
    """
    try:
        response = requests.get(host, timeout=os.getenv('TIMEOUT', 10))
        return {
            "status": response.status_code,
            "phrase": response.reason
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    transport = os.getenv("TRANSPORT", "streamable-http")
    mcp.run(transport=transport)