import allure

from pages.api_client import ApiClient

EXPECTED_CURRENCIES = ["USD", "EUR", "RUB", "GBP", "UAH", "TRY", "CNY", "JPY", "CAD", "CHF"]


@allure.feature("Currencies")
@allure.story("Integration")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_12_currencies_match_catalog(api_client: ApiClient):
    """TC-12: Список валют совпадает с конвертацией в каталоге"""
    with allure.step("GET /api/v1/currencies"):
        resp = api_client.currencies()
        assert resp.status_code == 200
        items = resp.json()["items"]

    currency_codes = [item["code"] for item in items]
    allure.attach(str(currency_codes), name="currency_codes", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"Проверить полноту списка ({len(EXPECTED_CURRENCIES)} валют)"):
        for code in EXPECTED_CURRENCIES:
            assert code in currency_codes, f"Currency '{code}' not found"
        assert len(currency_codes) == len(EXPECTED_CURRENCIES), \
            f"Expected {len(EXPECTED_CURRENCIES)} currencies, got {len(currency_codes)}"

    with allure.step("Для каждой валюты: GET /api/v1/catalog?currency={code}"):
        for code in currency_codes:
            catalog_resp = api_client.catalog(currency=code)
            assert catalog_resp.status_code == 200, f"Failed for currency={code}"
            data = catalog_resp.json()
            assert data["currency"] == code, f"Expected currency={code}, got {data['currency']}"
            if len(data["items"]) > 0:
                assert data["items"][0]["price"]["currency"] == code, \
                    f"Expected item price currency={code}, got {data['items'][0]['price']['currency']}"
