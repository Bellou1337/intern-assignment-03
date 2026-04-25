import pytest
import requests
from pages.api_client import ApiClient

BASE_URL = "http://localhost:8080"


@pytest.fixture(scope="session")
def api_client():
    client = ApiClient(BASE_URL)
    return client


@pytest.fixture(scope="session", autouse=True)
def wait_for_server():
    for _ in range(30):
        try:
            resp = requests.get(f"{BASE_URL}/health", timeout=5)
            if resp.status_code == 200:
                return
        except requests.ConnectionError:
            pass
        import time
        time.sleep(2)
    raise RuntimeError(f"Server at {BASE_URL} is not ready after 60 seconds")
