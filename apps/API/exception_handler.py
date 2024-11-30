# from django.core.exceptions import (
#     ValidationError as DjangoValidationError,
#     PermissionDenied,
# )
# from django.http import Http404

# from rest_framework import exceptions
# from rest_framework.response import Response
# from rest_framework.views import exception_handler
# from rest_framework.serializers import as_serializer_error

# from apps.API.exception_class import ApplicationError


# # todo: auto log and email errors
# def custom_exception_handler(exc, ctx):
#     if isinstance(exc, DjangoValidationError):
#         exc = exceptions.ValidationError(as_serializer_error(exc))

#     if isinstance(exc, Http404):
#         exc = exceptions.NotFound()

#     if isinstance(exc, PermissionDenied):
#         exc = exceptions.PermissionDenied()

#     response = exception_handler(exc, ctx)

#     if response is None:
#         if isinstance(exc, ApplicationError):
#             data = {"message": exc.message, "extra": exc.extra}
#             return Response(data, status=exc.status_code)

#         return response

#     if isinstance(exc.detail, (list, dict)):
#         response.data = {"detail": response.data}

#     if isinstance(exc, exceptions.ValidationError):
#         response.data["message"] = "Validation error"
#         response.data["extra"] = {"fields": response.data["detail"]}

#     else:
#         response.data["message"] = response.data["detail"]
#         response.data["extra"] = {}

#     del response.data["detail"]

#     return response

from importlib import import_module

from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404
from django.conf import settings
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.serializers import as_serializer_error

from apps.API.base_response import DefaultResponseSchema
from apps.API.exception_class import ApplicationError


def get_response_schema_class():
    custom_class_path = getattr(settings, "CUSTOM_RESPONSE_SCHEMA_CLASS", None)
    if custom_class_path:
        try:
            module_path, class_name = custom_class_path.rsplit(".", 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Error importing {custom_class_path}: {e}")

    return DefaultResponseSchema


def custom_exception_handler(exc, ctx):
    # Get the response schema class
    response_schema_class = get_response_schema_class()
    response_schema = response_schema_class()

    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    if response is None:
        if isinstance(exc, ApplicationError):
            data = response_schema.format_response(exc.message, exc.extra)
            return Response(data, status=exc.status_code)

        return response

    if isinstance(exc.detail, (list, dict)):
        response_data = response_schema.format_response(
            "Validation error"
            if isinstance(exc, exceptions.ValidationError)
            else response.data["detail"],
            response.data if isinstance(exc, exceptions.ValidationError) else None,
        )
    else:
        response_data = response_schema.format_response(response.data["detail"])

    return Response(response_data, status=response.status_code)
