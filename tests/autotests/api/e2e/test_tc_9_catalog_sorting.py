import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("E2E")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_9_catalog_sorting(api_client: ApiClient):
    """TC-9: Сортировка каталога — проверка порядка товаров"""
    with allure.step("GET /api/v1/catalog?sort=price_asc"):
        resp = api_client.catalog(sort="price_asc")
        assert resp.status_code == 200
        data = resp.json()
        assert data["meta"]["sort"] == "price_asc"

    with allure.step("Проверить сортировку по возрастанию цены"):
        amounts = [item["price"]["amount"] for item in data["items"]]
        for i in range(len(amounts) - 1):
            assert amounts[i] <= amounts[i + 1], f"price_asc violated at index {i}: {amounts[i]} > {amounts[i + 1]}"

    with allure.step("GET /api/v1/catalog?sort=price_desc"):
        resp2 = api_client.catalog(sort="price_desc")
        assert resp2.status_code == 200
        data2 = resp2.json()
        assert data2["meta"]["sort"] == "price_desc"

    with allure.step("Проверить сортировку по убыванию цены"):
        amounts2 = [item["price"]["amount"] for item in data2["items"]]
        for i in range(len(amounts2) - 1):
            assert amounts2[i] >= amounts2[i + 1], f"price_desc violated at index {i}: {amounts2[i]} < {amounts2[i + 1]}"

    with allure.step("GET /api/v1/catalog?sort=rating_desc"):
        resp3 = api_client.catalog(sort="rating_desc")
        assert resp3.status_code == 200
        data3 = resp3.json()
        assert data3["meta"]["sort"] == "rating_desc"

    with allure.step("Проверить сортировку по убыванию рейтинга"):
        ratings = [item["rating"] for item in data3["items"]]
        for i in range(len(ratings) - 1):
            assert ratings[i] >= ratings[i + 1], f"rating_desc violated at index {i}: {ratings[i]} < {ratings[i + 1]}"
