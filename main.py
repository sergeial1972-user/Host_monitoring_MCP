import requests
from http import HTTPStatus
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HostMonitoring")


@mcp.tool()
def check_host(host: str) -> dict:
    """Check HTTP status of a host.

    Args:
        host: Full URL (https://example.com)
    """
    try:
        response = requests.get(host, timeout=10)
        return {
            "status": response.status_code,
            "phrase": response.reason
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
@mcp.tool()
def check_host(host: str) -> dict:

    try:
        response = requests.get(host, timeout=10)
        return {
            "status": response.status_code,
            "phrase": response.reason  # или "OK" для успеха
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

