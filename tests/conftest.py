import pytest
import yaml
from framework.api_client import APIClient
from framework.base_api import BaseAPI

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(config["base_url"])

@pytest.fixture
def base_api(api_client):
    return BaseAPI(api_client)

# ---------- TEST DATA FIXTURES ----------
@pytest.fixture(scope="session")
def weather_cities():
    return ["London", "Paris", "New York"]

@pytest.fixture(scope="session")
def invalid_api_key():
    return "INVALID_KEY"

@pytest.fixture(scope="session")
def invalid_city():
    return "FakeCity123"
