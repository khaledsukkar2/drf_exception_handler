from enum import Enum

class ResponseEnum(Enum):
    MESSAGE = "message"
    DATA = "data"
    ERRORS = "errors"
    EXTRA = "extra"