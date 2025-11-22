from typing import Dict, Any

from framework.api.base_api import BaseAPI


class WeatherAPI(BaseAPI):
    """
    Weather API wrapper that provides methods to interact with
    current weather and forecast endpoints.
    """

    def get_current_weather(self, city: str, api_key: str) -> Dict[str, Any]:
        """
        Fetch the current weather for a given city.

        Args:
            city (str): Name of the city (e.g., "London").
            api_key (str): API key for authentication.

        Returns:
            Dict[str, Any]: JSON response from the /weather endpoint.
        """
        params = {
            "q": city,
            "appid": api_key
        }
        return self.client.get("/weather", params=params)

    def get_forecast(self, lat: float, lon: float, api_key: str) -> Dict[str, Any]:
        """
        Fetch the weather forecast for given coordinates.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.
            api_key (str): API key for authentication.

        Returns:
            Dict[str, Any]: JSON response from the /forecast endpoint.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        return self.client.get("/forecast", params=params)
