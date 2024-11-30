
class ApplicationError(Exception):
    def __init__(self, message, extra=None, status_code=400):
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.extra = extra or {}


class CustomErrorClass(Exception):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)

        for key, value in kwargs:
            self.key = value
