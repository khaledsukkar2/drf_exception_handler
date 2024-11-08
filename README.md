To Do:
1. set the exception handler to our, on rest framework settings
2. you can use ValidationError, PermissionError and http404 freely and it will return in json
3. you can use inlince_exception to raise your own exceptions (schema and data and status code)
4. you can add your own exception schema like this:</br>
```py
class ApplicationError(Exception):
    def __init__(self, message, extra=None, status_code=400):
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.extra = extra or {}
```
You can add any number of attribute and whichever schema you want
and raise it in your business logic position like this:
```py
def trigger_application_error():
    raise ApplicationError(message="Something is not correct", extra={"type": "RANDOM"})
```
add it on our package settings

* we have to establish a way to check if the user provide a custom exception schema in our package settings and if provided switch it with our default AppilicationError (at apps/API/exception_class.py)

How To Create A New Django App In Our Project:

1. first create a new folder with the name of the new app inside apps folder</br>
e.g: New

2. then run this command on shell</br>
```bash
python manage.py startapp New apps/New
```

3. inside new_app/apps.py do this:</br>
```py
class NewConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.New"
    verbose_name = _("New App")
```

4. now it's time to re-structure the app folder and app files:
    1. delete views.py and tests.py
    2. add apis instead views.py in the folder:
        * apis can be file or folder that has many files.
    3. add urls.py file:
        * you have to add this urlpatterns from this file inside urls.py for the whole project at: `apps/API/urls.py`
    4. add services and selectors:
        * services and selectors can be files or folders that have many files
    
    5. add filters if you need filter class in your app:
        * filters can be file or folder that has many files (depending on your needs).
    6. add tests folder:
        * it have to contain fixtrues and factories folders
        * then for each testing type add folder</br>
        e.g: if you want to test services then add services folder that has the tests files, if you want to test models then add models folder that has the tests
    7. add management folder that holds the management commands for this app (or for the project)
    8. add initial_data folder that manages adding data on production server
    9. add readme.md that has the documentation of this app (talk about: what is this app and how it works `just shortcuts not full explaination`)
    10. if you need to work with celery taks, add celery tasks within tasks.py file
