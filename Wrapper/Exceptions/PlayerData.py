class GetFriendsException(Exception):
    """ Exception raised for request errors in get friends of a specific player request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 422:
            self.message = "Some data provided is invalid"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class GuildInformationException(Exception):
    """ Exception raised for request errors in get guild information request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class PlayerDataException(Exception):
    """ Exception raised for request errors in the player data request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class PlayerStatusException(Exception):
    """ Exception raised for request errors in get player status request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class RankedSkyWarsException(Exception):
    """ Exception raised for request errors in getting ranked SkyWars rating and position request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 404:
            self.message = "No data could be found for the requested player"

        elif self.status_code == 422:
            self.message = "Some data provided is invalid"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class RecentlyPlayedException(Exception):
    """ Exception raised for request errors in get player's recent game request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 400:
            self.message = "Some data is missing, this is usually a field"

        elif self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 422:
            self.message = "Some data provided is invalid"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")
