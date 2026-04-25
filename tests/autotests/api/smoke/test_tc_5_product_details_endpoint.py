import allure

from pages.api_client import ApiClient


@allure.feature("Product Details")
@allure.story("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_5_product_details_endpoint(api_client: ApiClient):
    """TC-5: Получение карточки товара по ID"""
    with allure.step("GET /api/v1/catalog — получить первый товар"):
        catalog = api_client.catalog()
        assert catalog.status_code == 200
        items = catalog.json().get("items", [])
        assert len(items) > 0, "Catalog should have items"
        product_id = items[0]["id"]
        allure.attach(str(product_id), name="productId", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"GET /api/v1/catalog/{product_id}"):
        response = api_client.product_details(product_id)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    with allure.step("Проверить корневые поля"):
        assert "language" in data, "Missing 'language'"
        assert "currency" in data, "Missing 'currency'"
        assert "product" in data, "Missing 'product'"
        assert "reviews" in data, "Missing 'reviews'"
        assert "meta" in data, "Missing 'meta'"

    product = data["product"]
    with allure.step("Проверить структуру product"):
        assert product.get("id") == product_id, f"Expected id={product_id}, got {product.get('id')}"
        for field in ("title", "description", "price", "rating", "imageUrl", "category"):
            assert field in product, f"Missing '{field}' in product"

    reviews = data["reviews"]
    with allure.step("Проверить reviews"):
        assert isinstance(reviews, list), "reviews should be a list"
        for review in reviews:
            for field in ("id", "rating", "comment", "date", "reviewerName"):
                assert field in review, f"Missing '{field}' in review"
