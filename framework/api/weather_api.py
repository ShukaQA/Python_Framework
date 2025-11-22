from framework.api.base_api import BaseAPI


class WeatherAPI(BaseAPI):

    def get_current_weather(self, city, api_key):
        params = {
            "q": city,
            "appid": api_key
        }
        return self.client.get("/weather", params=params)

    def get_forecast(self, lat, lon, api_key):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        return self.client.get("/forecast", params=params)
