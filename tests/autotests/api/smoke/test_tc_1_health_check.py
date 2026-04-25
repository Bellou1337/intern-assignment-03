import allure

from pages.api_client import ApiClient


@allure.feature("Health")
@allure.story("Smoke")
@allure.severity(allure.severity_level.BLOCKER)
def test_tc_1_health_check(api_client: ApiClient):
    """TC-1: Health Check — сервер доступен"""
    response = api_client.health()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data.get("status") == "ok", f"Expected status=ok, got {data}"
