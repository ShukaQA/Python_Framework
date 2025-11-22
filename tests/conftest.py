import pytest
import yaml

from framework.api.weather_api import WeatherAPI
from framework.helper.api_client import APIClient


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(config["base_url"])


@pytest.fixture(scope="session")
def weather_api(api_client):
    return WeatherAPI(api_client)


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
