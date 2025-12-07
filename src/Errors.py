# Defining the Error Classes


class InvalidServiceName(Exception):
    # Raised when the Service Name entered is Invalid
    pass


class NetworkError(Exception):
    # Raised when there are network/connection issues
    pass
