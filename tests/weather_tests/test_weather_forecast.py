from framework.utils import assert_status_code


def test_forecast_weather(weather_api, config, weather_cities):
    for city in weather_cities:

        # Get current weather -> extract coordinates
        current = weather_api.get_current_weather(city, config["api_key"])
        assert_status_code(current, 200)

        coords = current.json()["coord"]
        lat, lon = coords["lat"], coords["lon"]

        # Get forecast
        forecast = weather_api.get_forecast(lat, lon, config["api_key"])
        assert_status_code(forecast, 200)

        data = forecast.json()
        assert "city" in data
        assert city in data["city"]["name"]
