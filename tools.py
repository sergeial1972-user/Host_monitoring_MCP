import requests
from http import HTTPStatus

def check_host(host, timeout = 10):
    try:
        response = requests.get(host, timeout=timeout)
        return HTTPStatus(response.status_code).phrase, response.status_code
    except requests.exceptions.RequestException as e:
        return f"CONNECTION ERROR: {e}", None

