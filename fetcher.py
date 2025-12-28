import requests
from config import HEADERS

def fetch_page(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status() # https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/
    return response.text
