from framework.utils import assert_status_code, assert_json_has_keys

def test_current_weather(base_api, config, weather_cities):
    for city in weather_cities:
        params = {
            "q": city,
            "appid": config["api_key"]
        }

        response = base_api.client.get("/weather", params=params)

        assert_status_code(response, 200)

        data = response.json()
        assert_json_has_keys(data, ["weather", "main", "wind", "name"])
        assert city in data["name"]
