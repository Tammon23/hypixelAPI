class InvalidAPIKeyError(Exception):
    """Exception raised when an api key is not in the system"""

    def __init__(self):
        super().__init__("No information related to API Key in Hypixel API")


class UnknownUsernameError(Exception):
    """Exception raised when the username does not exist"""

    def __init__(self):
        super().__init__("Unknown username")
