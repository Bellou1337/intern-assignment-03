import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Regression")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_19_nonexistent_category(api_client: ApiClient):
    """TC-19: Фильтрация по несуществующей категории — пустой результат"""
    with allure.step("GET /api/v1/catalog?category=nonexistent-category"):
        response = api_client.catalog(category="nonexistent-category")
        assert response.status_code == 200

    data = response.json()
    assert len(data["items"]) == 0, "Items should be empty for nonexistent category"
    assert data["meta"]["category"] == "nonexistent-category"
    assert data["meta"]["totalProducts"] == 0
