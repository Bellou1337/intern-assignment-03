import allure

from pages.api_client import ApiClient


@allure.feature("Catalog")
@allure.story("E2E")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc_10_currency_conversion(api_client: ApiClient):
    """TC-10: Конвертация валют — сравнение цен в разных валютах"""
    with allure.step("GET /api/v1/catalog?currency=USD"):
        resp_usd = api_client.catalog(currency="USD")
        assert resp_usd.status_code == 200
        data_usd = resp_usd.json()
        assert data_usd["currency"] == "USD"

    items_usd = data_usd["items"]
    assert len(items_usd) > 0
    first_id = items_usd[0]["id"]
    usd_price = items_usd[0]["price"]["amount"]
    assert items_usd[0]["price"]["currency"] == "USD"

    with allure.step("GET /api/v1/catalog?currency=EUR"):
        resp_eur = api_client.catalog(currency="EUR")
        assert resp_eur.status_code == 200
        data_eur = resp_eur.json()
        assert data_eur["currency"] == "EUR"

    items_eur = data_eur["items"]
    eur_item = next((i for i in items_eur if i["id"] == first_id), None)
    assert eur_item is not None, f"Product {first_id} not found in EUR catalog"
    eur_price = eur_item["price"]["amount"]
    assert eur_item["price"]["currency"] == "EUR"

    with allure.step("Проверить что цены в разных валютах отличаются"):
        assert usd_price != eur_price, f"USD price {usd_price} should differ from EUR price {eur_price}"

    with allure.step(f"GET /api/v1/catalog/{first_id}?currency=EUR"):
        detail_eur = api_client.product_details(first_id, currency="EUR")
        assert detail_eur.status_code == 200
        detail_data = detail_eur.json()

    with allure.step("Проверить цену в карточке товара"):
        assert detail_data["product"]["price"]["currency"] == "EUR"
        assert detail_data["product"]["price"]["amount"] == eur_price, \
            f"Detail EUR price {detail_data['product']['price']['amount']} != catalog EUR price {eur_price}"
