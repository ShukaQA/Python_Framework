from framework.utils import assert_status_code


def test_invalid_city(weather_api, config, invalid_city):
    response = weather_api.get_current_weather(invalid_city, config["api_key"])
    assert_status_code(response, 404)
