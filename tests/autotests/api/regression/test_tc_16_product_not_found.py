import allure

from pages.api_client import ApiClient


@allure.feature("Product Details")
@allure.story("Regression")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_16_product_not_found(api_client: ApiClient):
    """TC-16: Несуществующий товар — 404"""
    with allure.step("GET /api/v1/catalog/999999999"):
        response = api_client.product_details("999999999")
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    data = response.json()
    assert data.get("statusCode") == 404, f"Expected statusCode=404, got {data.get('statusCode')}"
    assert data.get("error") == "PRODUCT_NOT_FOUND", f"Expected error=PRODUCT_NOT_FOUND, got {data.get('error')}"
    assert "message" in data, "Error should have 'message' field"
