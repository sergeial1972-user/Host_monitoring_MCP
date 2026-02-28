#imports
import requests

def check_host(host):
    url = host
    try:
        response = requests.get(url)
        if response.status_code == 100:
            return "Continue", response.status_code
        elif response.status_code == 102:
            return "Switching Protocols", response.status_code
        elif response.status_code == 103:
            return "Early Hints", response.status_code
        elif response.status_code == 200:
            return "OK", response.status_code
        elif response.status_code == 201:
            return "Created", response.status_code
        elif response.status_code == 202:
            return "Accepted", response.status_code
        elif response.status_code == 203:
            return "Non-Authoritative Information", response.status_code
        elif response.status_code == 204:
            return "No Content", response.status_code
        elif response.status_code == 205:
            return "Reset Content", response.status_code
        elif response.status_code == 206:
            return "Partial Content", response.status_code
        elif response.status_code == 207:
            return "Multi-Status", response.status_code
        elif response.status_code == 208:
            return "Already Reported", response.status_code
        elif response.status_code == 226:
            return "IM Used", response.status_code
        elif response.status_code == 300:
            return "Multiple Choices", response.status_code
        elif response.status_code == 301:
            return "Moved Permanently", response.status_code
        elif response.status_code == 302:
            return "Found", response.status_code
        elif response.status_code == 303:
            return "See Other", response.status_code
        elif response.status_code == 304:
            return "Not Modified", response.status_code
        elif response.status_code == 305:
            return "Use Proxy", response.status_code
        elif response.status_code == 306:
            return "No Longer Used", response.status_code
        elif response.status_code == 307:
            return "Temporary Redirect", response.status_code
        elif response.status_code == 308:
            return "Moved Permanently", response.status_code
        elif response.status_code == 400:
            return "Bad Request", response.status_code
        elif response.status_code == 401:
            return "Unauthorized", response.status_code
        elif response.status_code == 402:
            return "Payment Required", response.status_code
        elif response.status_code == 403:
            return "Forbidden", response.status_code
        elif response.status_code == 404:
            return "Not Found", response.status_code
        elif response.status_code == 405:
            return "Method Not Allowed", response.status_code
        elif response.status_code == 406:
            return "Not Acceptable", response.status_code
        elif response.status_code == 407:
            return "Proxy authentication required", response.status_code
        elif response.status_code == 408:
            return "Request timed out", response.status_code
        elif response.status_code == 409:
            return "Conflict", response.status_code
        elif response.status_code == 410:
            return "Gone", response.status_code
        elif response.status_code == 411:
            return "Length Required", response.status_code
        elif response.status_code == 412:
            return "Precondition Required", response.status_code
        elif response.status_code == 413:
            return "Payload Too Large", response.status_code
        elif response.status_code == 414:
            return "Request Entity Too Large", response.status_code
        elif response.status_code == 415:
            return "Unsupported Media Type", response.status_code
        elif response.status_code == 416:
            return "Requested Range Not Satisfiable", response.status_code
        elif response.status_code == 417:
            return "Expectation Failed", response.status_code
        elif response.status_code == 421:
            return "Misdirect Request", response.status_code
        elif response.status_code == 422:
            return "Unprocessable Entity", response.status_code
        elif response.status_code == 423:
            return "Locked", response.status_code
        elif response.status_code == 424:
            return "Failed Dependency", response.status_code
        elif response.status_code == 425:
            return "too Early", response.status_code
        elif response.status_code == 426:
            return "Upgrade Required", response.status_code
        elif response.status_code == 428:
            return "Precondition Required", response.status_code
        elif response.status_code == 429:
            return "Too Many Requests", response.status_code
        elif response.status_code == 431:
            return "Request Header Too Large", response.status_code
        elif response.status_code == 451:
            return "Unavailable For Legal Reasons", response.status_code
        elif response.status_code == 500:
            return "Internal Server Error", response.status_code
        elif response.status_code == 501:
            return "Not Implemented", response.status_code
        elif response.status_code == 502:
            return "Bad Gateway", response.status_code
        elif response.status_code == 503:
            return "Service Unavailable", response.status_code
        elif response.status_code == 504:
            return "Gateway Timeout", response.status_code
        elif response.status_code == 505:
            return "HTTP Version Not Supported", response.status_code
        elif response.status_code == 507:
            return "Insufficient Not Supported", response.status_code
        elif response.status_code == 508:
            return "Loop Detected", response.status_code
        elif response.status_code == 510:
            return "Not extended", response.status_code
        elif response.status_code == 511:
            return "Network Authentication Required", response.status_code
        else:
            return "Internal Server Error", response.status_code