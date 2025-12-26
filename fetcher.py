import requests

# User-Agent is mandatory, otherwise it can be clocked
# About User-Agent: https://developer.mozilla.org/ru/docs/Web/HTTP/Reference/Headers/User-Agent
HEADERS = {
    'User_Agent': 'Mozilla/5.0'
}

def fetch_page(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status() # https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/
    return response.text
