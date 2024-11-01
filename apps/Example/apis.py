from django.http import Http404
from django.core.exceptions import ValidationError, PermissionDenied

from rest_framework.request import Request
from rest_framework import decorators, status, exceptions


@decorators.api_view(http_method_names=["get"])
def validation_error(request: Request):
    raise ValidationError("it's validation error")


@decorators.api_view(http_method_names=["get"])
def permission_denied(request: Request):
    raise PermissionDenied("it's permission denied")


@decorators.api_view(http_method_names=["get"])
def not_found(request: Request):
    raise Http404("it's HTTP404")


class TooManyRequest(exceptions.APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_code = "Many Request"
    default_detail = "This resource is closed because you call it too many times"


@decorators.api_view(http_method_names=["get"])
def too_many_request(request: Request):
    raise TooManyRequest()


def create_exception_class(attrs: dict):
    return type("inline_api_exception", (exceptions.APIException, ), attrs)

def inline_exception(attrs: dict):
    Exceptionklass = create_exception_class(attrs=attrs)
    return Exceptionklass


@decorators.api_view(http_method_names=["get"])
def inline_too_many_requests(request: Request):
    TooManyRequest = inline_exception(dict(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        default_code="Many Request",
        default_detail="This resource is closed because you call it too many times"
    ))

    raise TooManyRequest
