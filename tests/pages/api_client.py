import allure
import requests


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        with allure.step(f"{method} {path}"):
            response = self.session.request(
                method, url, timeout=self.timeout, **kwargs
            )
            body = response.text[:2000] if response.text else ""
            allure.attach(
                f"Status: {response.status_code}\nBody: {body}",
                name="Response",
                attachment_type=allure.attachment_type.TEXT,
            )
        return response

    def health(self) -> requests.Response:
        return self._request("GET", "/health")

    def languages(self) -> requests.Response:
        return self._request("GET", "/api/v1/languages")

    def currencies(self) -> requests.Response:
        return self._request("GET", "/api/v1/currencies")

    def catalog(self, **params) -> requests.Response:
        query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
        path = "/api/v1/catalog"
        if query:
            path += f"?{query}"
        return self._request("GET", path)

    def product_details(self, product_id: str, **params) -> requests.Response:
        query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
        path = f"/api/v1/catalog/{product_id}"
        if query:
            path += f"?{query}"
        return self._request("GET", path)
