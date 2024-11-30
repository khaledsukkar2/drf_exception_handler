from abc import ABC, abstractmethod
from .enums import ResponseEnum


class BaseResponseSchema(ABC):
    @abstractmethod
    def format_response(self, message, data=None, errors=None):
        pass

    def set_message(self, response_data, message):
        response_data[ResponseEnum.MESSAGE.value] = message

    def set_data(self, response_data, data):
        response_data[ResponseEnum.DATA.value] = data

    def set_errors(self, response_data, errors):
        response_data[ResponseEnum.ERRORS.value] = errors

    def set_extra(self, response_data, extra):
        response_data[ResponseEnum.EXTRA.value] = extra


## The styleguide response schema as default
class DefaultResponseSchema(BaseResponseSchema):
    def format_response(self, message, data=None, errors=None):
        response = {}
        self.set_message(response, message)
        self.set_extra(response, {"data": data, "errors": errors})
        return response
