class ShipException(Exception):
    """Ship exception."""

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class GoodException(Exception):
    """Exception for handling goods"""

    def __init__(self, status_code, message, type):
        self.status_code = status_code
        self.message = message
        self.type = type
