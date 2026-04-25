import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("E2E")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_8_catalog_pagination(api_client: ApiClient):
    """TC-8: Пагинация каталога — последовательный перебор страниц"""
    with allure.step("GET /api/v1/catalog?pageSize=5"):
        resp = api_client.catalog(pageSize=5)
        assert resp.status_code == 200
        data = resp.json()

    meta = data["meta"]
    with allure.step("Проверить первую страницу"):
        assert meta["currentPage"] == 1
        assert meta["pageSize"] == 5
        assert len(data["items"]) <= 5
        assert meta["totalProducts"] > 5, "Need >5 products for pagination test"
        total_pages = meta["totalPages"]
        assert total_pages > 1
        page1_ids = [item["id"] for item in data["items"]]

    with allure.step("GET /api/v1/catalog?pageSize=5&page=2"):
        resp2 = api_client.catalog(pageSize=5, page=2)
        assert resp2.status_code == 200
        data2 = resp2.json()

    with allure.step("Проверить вторую страницу"):
        assert data2["meta"]["currentPage"] == 2
        assert len(data2["items"]) <= 5
        page2_ids = [item["id"] for item in data2["items"]]
        assert page2_ids[0] != page1_ids[0], "Page 2 should have different items"

    with allure.step(f"GET /api/v1/catalog?pageSize=5&page={total_pages}"):
        resp_last = api_client.catalog(pageSize=5, page=total_pages)
        assert resp_last.status_code == 200
        data_last = resp_last.json()
        assert data_last["meta"]["currentPage"] == total_pages

    with allure.step(f"GET /api/v1/catalog?pageSize=5&page={total_pages + 1}"):
        resp_beyond = api_client.catalog(pageSize=5, page=total_pages + 1)
        assert resp_beyond.status_code == 200
        data_beyond = resp_beyond.json()
        assert len(data_beyond["items"]) == 0, "Items should be empty beyond last page"
        assert data_beyond["meta"]["currentPage"] == total_pages + 1
