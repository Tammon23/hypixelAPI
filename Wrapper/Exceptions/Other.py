class ActiveBoostersException(Exception):
    """ Exception raised for request errors in getting the active boosters list request

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


class CurrentLeaderboardsException(Exception):
    """ Exception raised for request errors in getting the current leaderboards request

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

        elif self.status_code == 503:
            self.message = "The data is not yet populated and should be available shortly"

        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")


class CurrentPlayerCountException(Exception):
    """ Exception raised for request errors in getting the current player count request

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


class PunishmentStatisticsException(Exception):
    """ Exception raised for request errors in getting the punishment statistics request

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

        elif self.status_code == 503:
            self.message = "The data is not yet populated and should be available shortly"

        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message}")
