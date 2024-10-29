from django.http import Http404
from django.core.exceptions import ValidationError, PermissionDenied

from rest_framework import decorators
from rest_framework.request import Request


@decorators.api_view(http_method_names=["get"])
def validation_error(request: Request):
    raise ValidationError("it's validation error")


@decorators.api_view(http_method_names=["get"])
def permission_denied(request: Request):
    raise PermissionDenied("it's permission denied")


@decorators.api_view(http_method_names=["get"])
def not_found(request: Request):
    raise Http404("it's HTTP404")
