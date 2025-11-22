from framework.utils import assert_status_code, assert_json_has_keys


def test_current_weather(weather_api, config, weather_cities):
    for city in weather_cities:
        response = weather_api.get_current_weather(city, config["api_key"])

        assert_status_code(response, 200)

        data = response.json()
        assert_json_has_keys(data, ["weather", "main", "wind", "name"])
        assert city in data["name"]
