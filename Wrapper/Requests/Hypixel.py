import requests
from .Requests import Requests


class Hypixel:
    def __init__(self, apikey: str):
        self.apikey = apikey
        self.BASE_URI = "https://api.hypixel.net/"

    def makeRequest(self, relative_uri):
        r = requests.get(f"{self.BASE_URI}{relative_uri}", params={"key": self.apikey})
        return Requests(r.json(), r.status_code)
