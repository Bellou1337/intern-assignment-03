import allure

from pages.api_client import ApiClient


@allure.feature("Languages")
@allure.story("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_2_languages_endpoint(api_client: ApiClient):
    """TC-2: Получение списка поддерживаемых языков"""
    with allure.step("GET /api/v1/languages"):
        response = api_client.languages()
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    with allure.step("Проверить структуру items"):
        items = data.get("items", [])
        assert isinstance(items, list), f"items should be a list, got {type(items)}"
        assert len(items) > 0, "items should not be empty"

        for item in items:
            assert "code" in item, f"Missing 'code' in {item}"
            assert "name" in item, f"Missing 'name' in {item}"
            assert "isSourceLanguage" in item, f"Missing 'isSourceLanguage' in {item}"

    with allure.step("Проверить наличие базового языка (en)"):
        en_lang = next((l for l in items if l["code"] == "en"), None)
        assert en_lang is not None, "Source language 'en' not found in languages"
        assert en_lang["isSourceLanguage"] is True, "en should be source language"
