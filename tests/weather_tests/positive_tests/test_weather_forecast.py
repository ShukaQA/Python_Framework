import pytest

from framework.logger import logger
from framework.utils import assert_status_code

@pytest.mark.positive_tests
def test_forecast_weather(weather_api, config, weather_cities):
    """
    Verify that the forecast API returns correct data for a list of cities.
    The test first retrieves the current weather to extract the city's coordinates,
    then requests the forecast using these coordinates.
    """
    for city in weather_cities:
        logger.info(f"Requesting current weather for city: {city}")

        # Step 1: Get current weather to obtain coordinates
        current_response = weather_api.get_current_weather(city, config["api_key"])
        assert_status_code(current_response, 200)
        logger.info(f"Current weather retrieved for city: {city}")

        coords = current_response.json().get("coord", {})
        lat, lon = coords.get("lat"), coords.get("lon")
        assert lat is not None and lon is not None, f"Coordinates missing for city: {city}"

        # Step 2: Request forecast using coordinates
        logger.info(f"Requesting forecast for city: {city} (lat={lat}, lon={lon})")
        forecast_response = weather_api.get_forecast(lat, lon, config["api_key"])
        assert_status_code(forecast_response, 200)

        forecast_data = forecast_response.json()
        assert "city" in forecast_data, f"'city' key missing in forecast data for {city}"
        assert city in forecast_data["city"]["name"], (
            f"Expected city '{city}' in forecast, got '{forecast_data['city']['name']}'"
        )

        logger.info(f"Forecast data verified for city: {city}")
