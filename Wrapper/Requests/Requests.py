from typing import Tuple, Optional, Any

import requests

from Wrapper.Exceptions.API import InvalidAPIException


class HypixelRequestMaker:
    def __init__(self, apiKey: str = None):
        self.api_key = apiKey
        self.BASE_URI = "https://api.hypixel.net"

    def _makeRequest(self, relative_uri: str, params: Optional[dict] = None, apiKeyNeeded: bool = True) -> Tuple[
        int, Any]:
        """ Helper functions using to make requests

        :param str relative_uri: The path to access the data via HypixelModels's API
        :param params: The dictionary of request parameters
        :type params: None or dict
        :param bool apiKeyNeeded: Whether the API key is needed to make a successful request
        :return: The request response
        :rtype: requests.Response
        :raises InvalidAPIException: if the api_key set on init is missing
        """
        if params is None:
            params = {}

        if apiKeyNeeded:
            if "key" not in params or params["key"] is None:
                if self.api_key is None:
                    raise InvalidAPIException()

                params["key"] = self.api_key

        r = requests.get(f"{self.BASE_URI}{relative_uri}", params=params)

        if r.status_code == 200:
            if "RateLimit-Limit" in r.headers and r.headers["RateLimit-Limit"] is not None:
                self.rateLimit = int(r.headers["RateLimit-Limit"])

            if "RateLimit-Remaining" in r.headers and r.headers["RateLimit-Remaining"] is not None:
                self.rateLimitRemaining = int(r.headers["RateLimit-Remaining"])

            if "RateLimit-Reset" in r.headers and r.headers["RateLimit-Reset"] is not None:
                self.rateLimitReset = int(r.headers["RateLimit-Reset"])

        return r.status_code, r.json()


class MojangRequestMaker:
    def __init__(self, response: str = None, status_code: int = None):
        self.response = response
        self.status_code = status_code
