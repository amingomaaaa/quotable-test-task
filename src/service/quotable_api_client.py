import requests


class QuotableAPIClient:
    _BASE_URL = "https://api.quotable.io"

    @classmethod
    def send_get_request(cls, endpoint: str) -> requests.Response:
        """Sends a GET request to the specified endpoint and returns the response"""
        url = f"{cls._BASE_URL}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response
