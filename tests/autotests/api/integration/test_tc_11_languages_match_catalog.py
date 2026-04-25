import allure

from pages.api_client import ApiClient

EXPECTED_LANGUAGES = ["en", "ru", "de", "fr", "es", "it", "pt", "tr", "uk", "zh"]


@allure.feature("Languages")
@allure.story("Integration")
@allure.severity(allure.severity_level.NORMAL)
def test_tc_11_languages_match_catalog(api_client: ApiClient):
    """TC-11: Список языков совпадает с поддерживаемыми в каталоге"""
    with allure.step("GET /api/v1/languages"):
        resp = api_client.languages()
        assert resp.status_code == 200
        items = resp.json()["items"]

    lang_codes = [item["code"] for item in items]
    allure.attach(str(lang_codes), name="language_codes", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"Проверить полноту списка ({len(EXPECTED_LANGUAGES)} языков)"):
        for code in EXPECTED_LANGUAGES:
            assert code in lang_codes, f"Language '{code}' not found in languages list"
        assert len(lang_codes) == len(EXPECTED_LANGUAGES), \
            f"Expected {len(EXPECTED_LANGUAGES)} languages, got {len(lang_codes)}"

    with allure.step("Для каждого языка: GET /api/v1/catalog?lang={code}"):
        for code in lang_codes:
            catalog_resp = api_client.catalog(lang=code)
            assert catalog_resp.status_code == 200, f"Failed for lang={code}"
            assert catalog_resp.json()["language"] == code, \
                f"Expected language={code}, got {catalog_resp.json()['language']}"
