class ActiveAuctionsException(Exception):
    """ Exception raised for request errors in getting a SkyBlock active auctions request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 404:
            self.message = "No data could be found for the requested player"

        elif self.status_code == 422:
            self.message = "Some data provided is invalid"

        elif self.status_code == 503:
            self.message = "The data is not yet populated and should be available shortly"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class AuctionByUUIDException(Exception):
    """ Exception raised for request errors in getting a SkyBlock auction(s) by a auction, player, or profile UUID request

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


class BazaarException(Exception):
    """ Exception raised for request errors in getting a SkyBlock Bazaar request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 503:
            self.message = "The data is not yet populated and should be available shortly"

        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class NewsException(Exception):
    """ Exception raised for request errors in getting SkyBlock news request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code):
        self.status_code = status_code
        self.message = None

        if self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class ProfileByUUIDException(Exception):
    """ Exception raised for request errors in getting a SkyBlock profile using an uuid request

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


class ProfileByPlayerException(Exception):
    """ Exception raised for request errors in getting a SkyBlock profile by player request

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
