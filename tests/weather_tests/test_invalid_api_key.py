from framework.utils import assert_status_code


def test_invalid_api_key(weather_api, invalid_api_key, weather_cities):
    city = weather_cities[0]

    response = weather_api.get_current_weather(city, invalid_api_key)

    assert_status_code(response, 401)
