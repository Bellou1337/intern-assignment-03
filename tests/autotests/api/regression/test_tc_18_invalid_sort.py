import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Regression")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_18_invalid_sort(api_client: ApiClient):
    """TC-18: Некорректный параметр сортировки"""
    with allure.step("GET /api/v1/catalog?sort=invalid"):
        response = api_client.catalog(sort="invalid")
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    data = response.json()
    assert data.get("statusCode") == 400
    assert data.get("error") == "BAD_REQUEST"
    assert "message" in data, "Error should have 'message' field"
