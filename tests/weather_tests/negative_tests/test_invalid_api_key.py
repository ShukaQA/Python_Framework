import pytest

from framework.logger import logger
from framework.utils import assert_status_code

@pytest.mark.negative_tests
def test_invalid_api_key(weather_api, invalid_api_key, weather_cities):
    """
    Verify that the API returns 401 Unauthorized when an invalid API key is used.
    """
    city = weather_cities[0]  # pick first city from fixture
    logger.info(f"Testing invalid API key for city: {city}")

    response = weather_api.get_current_weather(city, invalid_api_key)

    # Assert status code with logging
    assert_status_code(response, 401)
    logger.info(f"Received expected 401 Unauthorized for city: {city}")
