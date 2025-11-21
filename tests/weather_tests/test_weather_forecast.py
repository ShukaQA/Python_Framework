import pytest
from framework.utils import assert_status_code

def test_forecast_weather(base_api, config, weather_cities):
    """
    Test the forecast API for multiple cities using fixture-based test data.
    """

    for city in weather_cities:
        # Step 1: Get current weather to extract coordinates
        current_params = {
            "q": city,
            "appid": config["api_key"]
        }
        current_response = base_api.client.get("/weather", params=current_params)
        assert_status_code(current_response, 200)

        current_data = current_response.json()
        lat, lon = current_data["coord"]["lat"], current_data["coord"]["lon"]

        # Step 2: Call forecast API using extracted coordinates
        forecast_params = {
            "lat": lat,
            "lon": lon,
            "appid": config["api_key"]
        }
        forecast_response = base_api.client.get("/forecast", params=forecast_params)
        assert_status_code(forecast_response, 200)

        # --- Step 3: Assertions on forecast response ---
        forecast_data = forecast_response.json()
        forecast_city_name = forecast_data["city"]["name"]

        assert "city" in forecast_data, f"'city' key missing in forecast data for {city}"
        assert city in forecast_city_name, f"Expected city '{city}' in forecast, got '{forecast_city_name}'"
