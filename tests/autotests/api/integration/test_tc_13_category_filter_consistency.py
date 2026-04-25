import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("Integration")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_13_category_filter_consistency(api_client: ApiClient):
    """TC-13: Категории из каталога совпадают с фильтрацией по категории"""
    with allure.step("GET /api/v1/catalog"):
        resp = api_client.catalog()
        assert resp.status_code == 200
        data = resp.json()
        categories = data["categories"]
        total_unfiltered = data["meta"]["totalProducts"]

    assert len(categories) > 0, "Should have categories"
    allure.attach(str([c["slug"] for c in categories]), name="categories", attachment_type=allure.attachment_type.TEXT)

    total_filtered = 0
    with allure.step("Для каждой категории: проверить фильтрацию"):
        for cat in categories:
            slug = cat["slug"]
            cat_resp = api_client.catalog(category=slug)
            assert cat_resp.status_code == 200
            cat_data = cat_resp.json()
            assert cat_data["meta"]["category"] == slug

            for item in cat_data["items"]:
                assert item["category"]["slug"] == slug, f"Item {item['id']} has wrong category"

            total_filtered += cat_data["meta"]["totalProducts"]

    with allure.step("Проверить что сумма по категориям >= total без фильтра"):
        assert total_filtered >= total_unfiltered, \
            f"Sum of filtered ({total_filtered}) < unfiltered total ({total_unfiltered})"
