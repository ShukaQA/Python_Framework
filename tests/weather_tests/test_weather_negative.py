import pytest
from framework.utils import assert_status_code

def test_invalid_api_key(base_api, invalid_api_key, weather_cities):
    """
    Test that the weather API returns 401 Unauthorized
    when an invalid API key is used.
    """
    city = weather_cities[0]  # pick the first city from the fixture
    params = {
        "q": city,
        "appid": invalid_api_key
    }
    response = base_api.client.get("/weather", params=params)
    assert_status_code(response, 401)

def test_invalid_city(base_api, config, invalid_city):
    """
    Test that the weather API returns 404 Not Found
    when a non-existent city is requested.
    """
    params = {
        "q": invalid_city,
        "appid": config["api_key"]
    }
    response = base_api.client.get("/weather", params=params)
    assert_status_code(response, 404)
