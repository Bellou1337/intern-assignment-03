import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Regression")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_14_invalid_lang(api_client: ApiClient):
    """TC-14: Несуществующий язык — ошибка валидации"""
    with allure.step("GET /api/v1/catalog?lang=invalid"):
        response = api_client.catalog(lang="invalid")
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"

    data = response.json()
    assert data.get("statusCode") == 400, f"Expected statusCode=400, got {data.get('statusCode')}"
    assert data.get("error") == "BAD_REQUEST", f"Expected error=BAD_REQUEST, got {data.get('error')}"
    assert "message" in data, "Error should have 'message' field"
