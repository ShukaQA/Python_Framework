import pytest

from framework.logger import logger
from framework.utils import assert_status_code

@pytest.mark.negative_tests
def test_invalid_city(weather_api, config, invalid_city):
    """
    Verify that the API returns 404 Not Found
    when a non-existent city is requested.
    """
    logger.info(f"Testing invalid city: {invalid_city}")

    response = weather_api.get_current_weather(invalid_city, config["api_key"])

    # Assert status code with logging
    assert_status_code(response, 404)
    logger.info(f"Received expected 404 Not Found for city: {invalid_city}")
