# Notes about django
"""
manage.py -> used to run commands
__init__.py -> tells python that the folder contains python code
asgi.py and wsgi.py -> provide hooks for web servers such as Apache or nginx whn django is
running on a live website
settings -> configures django project
urls.py -> routes web requests based on url
"""

"""
Creating django project:
1) Install python
2)a) if pip is working proceed to 3
2)b) if pip not working install with "py -3 -m ensurepip"
3) install django with "python -m pip install django"
4) go to project folder in cmd(windows) type "python -m django startproject wisdompets"
5) go to wisdom pets folder in the created project and type "python manage.py runserver"
6) go to web browser and type "localhost:8000" to access local django project :) 
"""

"""
Django app:
Is a component in a django project, each django app support a set of features to django project
The features have specific purposes such as providing features to a blog, wiki, forum, etc
"""

"""
Pieces of an App in django:
apps.py -> controls settings specific for this app
models.py -> provides data layer which django uses to construct database schema and queries
admin.py -> defines administrative interface that allows to see and edit data related to
the app
urls.py -> used to url routing
views.py -> defines logic and control flow for handling requests and defines the HTTP 
responses
tests.py -> used for writing unit tests 
migrations/ -> holds files which django uses to migrate the database as we create and change
our database schema over time 
"""

"""
Django uses MVC(Model-View-Controller architecture), but uses different names for these
4 pieces to understand:
URL patterns -> used to decide which view to pass the request handling 
views -> receives an http request as an argument and returns http response for the web server
to return
models -> class with attributes that define the schema and underlying structure of a database
table, provides methods to make queries 
templates -> help with the presentation layer of what HTML response will look like, each 
template is a html file with some python code
"""

"""
A model is a class inheriting from django.db.models.Model and defines database fields as 
class attributes. We can conceptualize models as spreadsheets
Field types: CharField, TextField, EmailField, URLField, IntegerField, DecimalField
BooleanField, DateTimeField, ForeignKey, ManyToManyField...
Fild attributes:
blank=True -> not required by default
maxlength -> maximal lenght of the field
choices -> limit values to be stored in the field
"""

"""
Migrations: generate scripts to change the database structure
When migrations are needed ?
Adding a model, adding a field, removing a field and changing a field
Initial migration: the first migration created for a new Django app will create tables for
the models that are defined
Commands for migrations:
makemigrations -> generates migration files for later use
migrate -> runs all migrations in the project to the current state
Unapplied migration: a created migration that hasn't been run 
"""

"""
A Django management command is a script that is run using manage.py
"""

"""
URL Pattern:
checks each pattern in order, if there is a match the corresponding view is called
if there is no match, an error is submitted -> HTTP 404
The first argument of path() is the path converter:
1)strings match literally, such as "adoptions/"
2)you can also have a "capture group", anything inside <>, things inside are treated as variables
<int:pet_id> -> "int" is the type we're expecting for, "pet_id" is the variable in which we're storing   
Second argument it's the view
Third argument it's the template's name
"""

"""
Django ORM: object representation of a record in the database
"""

"""
Template syntax
{{variable}} -> variable value is shown
{% tag %} -> template tag, for loops, ifs, etc...
{{variable|filter}} -> use template filter, take string as input and return string as output
"""