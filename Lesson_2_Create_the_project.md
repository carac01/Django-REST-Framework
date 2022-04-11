### Let's create the virtual environment and activate it

```commandline
python3 -m venv venv
source venv/bin/activate
```

Now we create the file with txt extension and call it requirements.txt
This will be the place where we identify the dependencies (libraries) for installation.

```commandline
django
djangorestframework
# Instrument for testing
pytest
# Integration with Django
pytest-django
# Generator of the test data
Faker
```

Let's install the dependencies.

```commandline
pip3 install -r requirements.txt
```

Now we are creating our project with the name _proyecto_.

```commandline
django-admin startproject proyecto .
```

Inside the project we may have a lot of applications. At the moment create _books_.

```commandline
python manage.py startapp books
```
