import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_4_catalog_endpoint(api_client: ApiClient):
    """TC-4: Получение каталога товаров (дефолтные параметры)"""
    with allure.step("GET /api/v1/catalog (default params)"):
        response = api_client.catalog()
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()

    with allure.step("Проверить корневые поля"):
        assert data.get("language") == "en", f"Expected language=en, got {data.get('language')}"
        assert data.get("currency") == "USD", f"Expected currency=USD, got {data.get('currency')}"
        assert "categories" in data, "Missing 'categories'"
        assert "items" in data, "Missing 'items'"
        assert "meta" in data, "Missing 'meta'"

    meta = data["meta"]
    with allure.step("Проверить дефолтные значения мета"):
        assert meta.get("currentPage") == 1, f"Expected currentPage=1, got {meta.get('currentPage')}"
        assert meta.get("pageSize") == 20, f"Expected pageSize=20, got {meta.get('pageSize')}"
        assert meta.get("sort") == "price_asc", f"Expected sort=price_asc, got {meta.get('sort')}"
        assert meta.get("sourceLanguage") == "en"
        assert meta.get("sourceCurrency") == "USD"

    items = data["items"]
    with allure.step("Проверить структуру items"):
        assert isinstance(items, list), "items should be a list"
        assert len(items) > 0, "items should not be empty"
        product = items[0]
        for field in ("id", "title", "description", "price", "rating", "imageUrl", "category"):
            assert field in product, f"Missing '{field}' in product"

        price = product["price"]
        assert "amount" in price, "Missing 'amount' in price"
        assert "currency" in price, "Missing 'currency' in price"

        category = product["category"]
        assert "slug" in category, "Missing 'slug' in category"
        assert "title" in category, "Missing 'title' in category"

    categories = data["categories"]
    with allure.step("Проверить категории"):
        assert isinstance(categories, list), "categories should be a list"
        assert len(categories) >= 1, "Should have at least 1 category"

    with allure.step("Проверить мета-данные пагинации"):
        assert meta.get("totalProducts", 0) >= 1, "totalProducts should be >= 1"
        assert meta.get("totalPages", 0) >= 1, "totalPages should be >= 1"
