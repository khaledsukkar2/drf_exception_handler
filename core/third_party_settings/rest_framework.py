
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'apps.API.exception_handler.custom_exception_handler'
}


### Example 
CUSTOM_RESPONSE_SCHEMA_CLASS = 'app_name.MyCustomResponseSchema'