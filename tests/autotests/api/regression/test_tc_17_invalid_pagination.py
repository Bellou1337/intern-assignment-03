import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Regression")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_17_invalid_page_parameters(api_client: ApiClient):
    """TC-17: Некорректные параметры пагинации"""
    with allure.step("GET /api/v1/catalog?page=0"):
        resp1 = api_client.catalog(page=0)
        assert resp1.status_code == 400, f"page=0: Expected 400, got {resp1.status_code}"
        data1 = resp1.json()
        assert data1["statusCode"] == 400
        assert data1["error"] == "BAD_REQUEST"

    with allure.step("GET /api/v1/catalog?page=-1"):
        resp2 = api_client.catalog(page=-1)
        assert resp2.status_code == 400, f"page=-1: Expected 400, got {resp2.status_code}"
        data2 = resp2.json()
        assert data2["statusCode"] == 400
        assert data2["error"] == "BAD_REQUEST"

    with allure.step("GET /api/v1/catalog?pageSize=0"):
        resp3 = api_client.catalog(pageSize=0)
        assert resp3.status_code == 400, f"pageSize=0: Expected 400, got {resp3.status_code}"
        data3 = resp3.json()
        assert data3["statusCode"] == 400
        assert data3["error"] == "BAD_REQUEST"

    with allure.step("GET /api/v1/catalog?pageSize=101"):
        resp4 = api_client.catalog(pageSize=101)
        assert resp4.status_code == 400, f"pageSize=101: Expected 400, got {resp4.status_code}"
        data4 = resp4.json()
        assert data4["statusCode"] == 400
        assert data4["error"] == "BAD_REQUEST"
