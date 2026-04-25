import allure

from pages.api_client import ApiClient


@allure.feature("Currencies")
@allure.story("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_3_currencies_endpoint(api_client: ApiClient):
    """TC-3: Получение списка поддерживаемых валют"""
    with allure.step("GET /api/v1/currencies"):
        response = api_client.currencies()
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    with allure.step("Проверить структуру items"):
        items = data.get("items", [])
        assert isinstance(items, list), f"items should be a list, got {type(items)}"
        assert len(items) > 0, "items should not be empty"

        for item in items:
            assert "code" in item, f"Missing 'code' in {item}"
            assert "name" in item, f"Missing 'name' in {item}"
            assert "symbol" in item, f"Missing 'symbol' in {item}"
            assert "isSourceCurrency" in item, f"Missing 'isSourceCurrency' in {item}"

    with allure.step("Проверить наличие базовой валюты (USD)"):
        usd = next((c for c in items if c["code"] == "USD"), None)
        assert usd is not None, "Source currency 'USD' not found"
        assert usd["isSourceCurrency"] is True, "USD should be source currency"
