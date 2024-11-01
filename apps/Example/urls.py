from django.urls import path, include

from apps.Example import apis


app_name = "example"

urlpatterns = [
    path("validation_error/", apis.validation_error, name="validation_error"),
    path("permission_denied/", apis.permission_denied, name="permission_denied"),
    path("not_found_error/", apis.not_found, name="not_found"),
    path("too_many_request/", apis.too_many_request, name="too_many_request"),
    path("inline_too_many_request/", apis.inline_too_many_requests, name="inline_too_many_request"),
]
