import allure

from pages.api_client import ApiClient


@allure.feature("Product Details")
@allure.story("Regression")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_20_product_localization_and_currency(api_client: ApiClient):
    """TC-20: Карточка товара — локализация и конвертация вместе"""
    with allure.step("GET /api/v1/catalog — получить первый товар"):
        catalog = api_client.catalog()
        assert catalog.status_code == 200
        items = catalog.json()["items"]
        assert len(items) > 0
        product_id = items[0]["id"]

    with allure.step(f"GET /api/v1/catalog/{product_id}?lang=de&currency=EUR"):
        resp_de = api_client.product_details(product_id, lang="de", currency="EUR")
        assert resp_de.status_code == 200
        data_de = resp_de.json()

    with allure.step("Проверить немецкую локализацию"):
        assert data_de["language"] == "de"
        assert data_de["currency"] == "EUR"
        assert data_de["product"]["price"]["currency"] == "EUR"
        assert len(data_de["product"]["title"]) > 0, "Title should not be empty"

    with allure.step(f"GET /api/v1/catalog/{product_id}?lang=en&currency=USD"):
        resp_en = api_client.product_details(product_id, lang="en", currency="USD")
        assert resp_en.status_code == 200
        data_en = resp_en.json()

    with allure.step("Проверить английскую локализацию"):
        assert data_en["language"] == "en"
        assert data_en["currency"] == "USD"
        assert data_en["product"]["price"]["currency"] == "USD"

    with allure.step("Сравнить цены в разных валютах"):
        eur_price = data_de["product"]["price"]["amount"]
        usd_price = data_en["product"]["price"]["amount"]
        assert eur_price != usd_price, f"EUR price {eur_price} should differ from USD price {usd_price}"
