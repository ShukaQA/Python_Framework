import requests
from typing import Optional, Dict, Any
from framework.logger import logger


class HttpClient:
    """
    A simple HTTP client wrapper around requests.Session
    to perform GET and POST requests with logging support.
    """

    def __init__(self, base_url: str):
        """
        Initialize the HTTP client with a base URL.

        Args:
            base_url (str): Base URL for all API requests.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _build_url(self, endpoint: str) -> str:
        """
        Construct the full URL for a given endpoint.

        Args:
            endpoint (str): API endpoint, e.g., '/weather'.

        Returns:
            str: Full URL.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """
        Send a GET request.

        Args:
            endpoint (str): API endpoint.
            params (dict, optional): Query parameters.
            headers (dict, optional): Custom headers.

        Returns:
            requests.Response: Response object.
        """
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, headers=headers)
        logger.info(f"{response.request} ---> : {response.url}")
        logger.info(f"Response <--- {response.status_code} : {response.reason}")
        return response
