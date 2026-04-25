import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("E2E")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_7_catalog_search_and_filter(api_client: ApiClient):
    """TC-7: Поиск товара по названию и фильтрация по категории"""
    with allure.step("GET /api/v1/catalog — получить категории и товар"):
        catalog = api_client.catalog()
        assert catalog.status_code == 200
        data = catalog.json()
        categories = data["categories"]
        items = data["items"]
        assert len(categories) > 0, "Should have categories"
        assert len(items) > 0, "Should have items"

    category_slug = categories[0]["slug"]
    search_query = items[0]["title"][:5].lower()

    with allure.step(f"GET /api/v1/catalog?query={search_query}"):
        search_resp = api_client.catalog(query=search_query)
        assert search_resp.status_code == 200
        search_data = search_resp.json()
        assert search_data["meta"]["query"] == search_query

    with allure.step("Проверить что результаты содержат поисковый запрос"):
        for item in search_data["items"]:
            title_match = search_query in item["title"].lower()
            desc_match = search_query in item.get("description", "").lower()
            assert title_match or desc_match, f"Item {item['id']} doesn't match query"

    with allure.step(f"GET /api/v1/catalog?category={category_slug}"):
        cat_resp = api_client.catalog(category=category_slug)
        assert cat_resp.status_code == 200
        cat_data = cat_resp.json()
        assert cat_data["meta"]["category"] == category_slug

    with allure.step("Проверить что все товары в выбранной категории"):
        for item in cat_data["items"]:
            assert item["category"]["slug"] == category_slug, f"Item {item['id']} has wrong category"

    with allure.step(f"GET /api/v1/catalog?query={search_query}&category={category_slug}"):
        combo_resp = api_client.catalog(query=search_query, category=category_slug)
        assert combo_resp.status_code == 200
        combo_data = combo_resp.json()

    with allure.step("Проверить что результаты удовлетворяют обоим условиям"):
        for item in combo_data["items"]:
            assert item["category"]["slug"] == category_slug
            title_match = search_query in item["title"].lower()
            desc_match = search_query in item.get("description", "").lower()
            assert title_match or desc_match, f"Item {item['id']} doesn't match combined filter"
