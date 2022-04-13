### Tests

Let's add pytest as an instrument for testing with Django configuration.
We create the file [_pytest.ini_](pytest.ini) in a main dir of our project with the next content.

```commandline
[pytest]
DJANGO_SETTINGS_MODULE = proyecto.settings

# Optional, but recommended
python_files = tests.py test_*.py *_tests.py
```

For the current project, we are going to keep all our tests in one dir with tests divided with applications.
Create a new directory inside _books_ folder with the name [_tests_](tests).
Finally, inside _books_ create the file with the name [_test_example.py_](tests/books/test_example.py).

```commandline
tests
    └── books
            └── test_example.py
```

By the default, _pytest_ finds the files with the _test_ in file name.
For example, _test_*.py_ or _*test.py_.
Test functions should be started with _test_, if you want to use classes, they should start with _Test_. 
Add the next content:

```python
# tests/books/test_example.py

# The functions should start with "test_"
def test_title():
    assert "the little prince" != "harry potter"
```

To execute all tests, just execute:

```commandline
pytest
```

It will inform you that the test was passed without any issues.

```commandline
=================================== test session starts ========================================
platform ... -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0
django: settings: proyecto.settings (from ini)
rootdir: ...\Django-REST-Framework, configfile: pytest.ini
plugins: Faker-13.3.4, django-4.5.2
collected 1 item                                                                                                                                                  

tests\books\test_example.py .                                                              [100%]

===================================== 1 passed in 0.45s =========================================
```
