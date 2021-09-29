class APIException(Exception):
    """ Exception raised for request errors in the API request

    Attributes:
        status_code -- the request status code that was thrown
        message -- explanation of the error
    """

    def __init__(self, status_code, cause):
        self.status_code = status_code
        self.message = None
        self.cause = cause

        if self.status_code == 403:
            self.message = "Access is forbidden, usually due to an invalid API key being used"

        elif self.status_code == 429:
            self.message = "A request limit has been reached, usually this is due to the limit on the key being " \
                           "reached but can also be triggered by a global throttle"
        else:
            self.message = "Unregistered status code"

        super().__init__(f"[{self.status_code}] {self.message} Cause: {self.cause}")


class InvalidAPIException(Exception):
    """ Exception raised for request errors regarding a missing or invalid api key """

    def __init__(self):
        super().__init__("Invalid or Missing API Key")
