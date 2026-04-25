import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("E2E")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_6_catalog_browsing_with_localization(api_client: ApiClient):
    """TC-6: Просмотр каталога — от списка к карточке товара с локализацией"""
    with allure.step("GET /api/v1/catalog?lang=ru"):
        response = api_client.catalog(lang="ru")
        assert response.status_code == 200

    data = response.json()
    with allure.step("Проверить язык ответа"):
        assert data.get("language") == "ru", f"Expected language=ru, got {data.get('language')}"
        assert data.get("meta", {}).get("sourceLanguage") == "en"

    items = data["items"]
    assert len(items) > 0, "Catalog should have items"

    first_item = items[0]
    with allure.step(f"Извлечь первый товар id={first_item['id']}"):
        allure.attach(str(first_item), name="first_item", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"GET /api/v1/catalog/{first_item['id']}?lang=ru"):
        detail = api_client.product_details(first_item["id"], lang="ru")
        assert detail.status_code == 200

    detail_data = detail.json()
    with allure.step("Проверить данные карточки"):
        assert detail_data.get("language") == "ru"
        product = detail_data["product"]
        assert product["id"] == first_item["id"], f"Product id mismatch"
        assert product["title"] == first_item["title"], "Title mismatch between catalog and details"
        assert product["category"]["slug"] == first_item["category"]["slug"], "Category slug mismatch"
