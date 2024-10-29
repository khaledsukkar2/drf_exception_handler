from django.urls import path, include

from apps.Example import apis


app_name = "example"

urlpatterns = [
    path("validation_error/", apis.validation_error, name="validation_error"),
    path("permission_denied/", apis.permission_denied, name="permission_denied"),
    path("not_found_error/", apis.not_found, name="not_found"),
]
