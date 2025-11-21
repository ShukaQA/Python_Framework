import requests
from framework.logger import logger


def _log_request(method, url, params=None, data=None, json_body=None):
    logger.info(f"➡ REQUEST: {method} {url}")
    if params:
        logger.info(f"  Query Params: {params}")
    if data:
        logger.info(f"  Data: {data}")
    if json_body:
        # Only print top-level keys for readability
        keys = ", ".join(json_body.keys()) if isinstance(json_body, dict) else str(json_body)
        logger.info(f"  JSON Body Keys: {keys}")


def _log_response(response):
    status = response.status_code
    url = response.url
    logger.info(f"⬅ RESPONSE: {status} {url}")

    try:
        body = response.json()
        # Only print summary: top-level keys, city name, coord if exists
        summary = {}
        for key in ["coord", "weather", "main", "wind", "clouds", "name"]:
            if key in body:
                summary[key] = body[key]
        logger.info(f"  Response Summary: {summary}")
    except Exception:
        # fallback if not JSON
        logger.info(f"  Response Text: {response.text}")


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        _log_request("GET", url, params=params)
        response = self.session.get(url, params=params)
        _log_response(response)
        return response

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        _log_request("POST", url, data=data, json_body=json)
        response = self.session.post(url, data=data, json=json)
        _log_response(response)
        return response
