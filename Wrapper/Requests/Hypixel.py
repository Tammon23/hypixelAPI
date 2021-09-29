from typing import Optional, Any, Tuple

import requests

from ..Exceptions.API import InvalidAPIException, APIException
from ..Hypixel.General.Leaderboards import Leaderboards
from ..Hypixel.General.PlayerCounts import PlayerCounts
from ..Hypixel.General.APIKey import APIKey
from ..Hypixel.General.Boosters import Boosters


class Hypixel:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.BASE_URI = "https://api.hypixel.net"
        self.rate_limit_reset = -1  # The time in seconds until the rate limit is reset
        self.rate_limit_remaining = -1  # The amount of requests left before reset
        self.rate_limit = -1

    def _makeRequest(self, relative_uri: str, params: Optional[dict] = None, api_key_needed: bool = True) -> Tuple[
        int, Any]:
        """ Helper functions using to make requests

        :param str relative_uri: The path to access the data via Hypixel's API
        :param params: The dictionary of request parameters
        :type params: None or dict
        :param bool api_key_needed: Whether the API key is needed to make a successful request
        :return: The request response
        :rtype: requests.Response
        :raises InvalidAPIException: if the api_key set on init is missing
        """
        if params is None:
            params = {}

        if api_key_needed:
            if "key" not in params or params["key"] is None:
                if self.api_key is None:
                    raise InvalidAPIException()

                params["key"] = self.api_key

        r = requests.get(f"{self.BASE_URI}{relative_uri}", params=params)

        if r.status_code == 200:
            if "RateLimit-Limit" in r.headers and r.headers["RateLimit-Limit"] is not None:
                self.rate_limit = int(r.headers["RateLimit-Limit"])

            if "RateLimit-Remaining" in r.headers and r.headers["RateLimit-Remaining"] is not None:
                self.rate_limit_remaining = int(r.headers["RateLimit-Remaining"])

            if "RateLimit-Reset" in r.headers and r.headers["RateLimit-Reset"] is not None:
                self.rate_limit_reset = int(r.headers["RateLimit-Reset"])

        return r.status_code, r.json()

    def api_key_data(self, api_key: Optional[str] = None) -> APIKey:
        """ Get api key information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the api key
        :rtype: APIKey
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/key", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/key")

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return APIKey.parse_obj(response["record"])

    def boosters(self, api_key: Optional[str] = None) -> Boosters:
        """ Get api key information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the api key
        :rtype: APIKey
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/boosters", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/boosters")

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return Boosters.parse_obj({"boosters": response["boosters"], "boosterState": response["boosterState"]})

    def playerCounts(self, api_key: Optional[str] = None) -> PlayerCounts:
        """ Get api key information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the api key
        :rtype: APIKey
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/counts", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/counts")

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return PlayerCounts.parse_obj({"games": response["games"], "playerCount": response["playerCount"]})

    def leaderboards(self, api_key: Optional[str] = None) -> Leaderboards:
        """ Get api key information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the api key
        :rtype: APIKey
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/leaderboards", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/`leaderboards`")

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return Leaderboards.parse_obj({"leaderboards": response["leaderboards"]})
