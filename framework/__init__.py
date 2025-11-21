import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")  # remove trailing slash if any
        self.session = requests.Session()

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        url = self._build_url(endpoint)
        logger.info(f"GET {url} | params={params}")
        response = self.session.get(url, params=params, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response

    def post(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        url = self._build_url(endpoint)
        logger.info(f"POST {url} | data={data} | json={json}")
        response = self.session.post(url, data=data, json=json, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response
