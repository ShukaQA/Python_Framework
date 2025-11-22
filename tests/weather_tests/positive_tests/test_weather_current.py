import pytest

from framework.logger import logger
from framework.utils import assert_status_code, assert_json_has_keys

@pytest.mark.positive_tests
def test_current_weather(weather_api, config, weather_cities):
    """
    Verify that the current weather API returns correct data
    for a list of valid cities.
    """
    for city in weather_cities:
        logger.info(f"Requesting current weather for city: {city}")

        response = weather_api.get_current_weather(city, config["api_key"])

        # Assert status code
        assert_status_code(response, 200)
        logger.info(f"Received 200 OK for city: {city}")

        # Assert response JSON structure
        data = response.json()
        assert_json_has_keys(data, ["weather", "main", "wind", "name"])
        assert city in data["name"], f"Expected city '{city}' in response, got '{data['name']}'"

        logger.info(f"Verified weather data for city: {city}")
