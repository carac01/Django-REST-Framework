### Simple GET

In the current lesson we will not use [Django REST Framework](https://www.django-rest-framework.org/), but _Django only_.
Let's create the classic ping-pong to check that the service is alive.
Realise the function [view](books/views.py) with response:

```python
# books/views.py

from django.http import JsonResponse

def ping(request):
    data = {"ping": "pong"}
    return JsonResponse(data)
```

Add the route to [urls.py](proyecto/urls.py):

```python
# proyecto/urls.py

from django.contrib import admin
from django.urls import path

from books.views import ping # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"), # new
]
```

Run the server:

```commandline
python manage.py runserver
```

And run the HTTP request from the terminal with curl to check that we got the expected result:

```commandline
curl http://127.0.0.1:8000/ping/
```

It will return the next response:

```commandline
$ curl http://127.0.0.1:8000/ping/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    16  100    16    0     0   8000      0 --:--:-- --:--:-- --:--:--  8000{"ping": "pong"}
```

At this moment create the new test. We create [test_ping.py](tests/books/test_ping.py):

```commandline
tests
    └── books
            └── test_example.py
                test_ping.py
```
```python
# tests/books/test_ping.py

import json
from django.urls import reverse


def test_ping(client):
    # Get the route "ping"
    url = reverse("ping")
    # Do GET with client
    response = client.get(url)
    # Receive JSON which converted in dictionary with json.loads() to handle it - 
    # it helps to verify content => '{"ping": "pong"}'
    content = json.loads(response.content)
    # Check the status code - it expected to be 200 OK
    assert response.status_code == 200
    # Does content with 'ping' key contain 'pong' value?
    assert content["ping"] == "pong"
```

_client_ is the fixture that helps _pytest-django_ which represent the instance _django.test.Client_.
Basically this is the HTTP client which we are going to apply inside the tests.
You already could run the test:

```commandline
pytest
```

```commandline
====================================== test session starts =================================================
platform ... -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0
django: settings: proyecto.settings (from ini)
rootdir: ...\Django-REST-Framework, configfile: pytest.ini
plugins: Faker-13.3.4, django-4.5.2
collected 2 items                                                                                                                                                 

tests\books\test_example.py .                                                                          [ 50%]
tests\books\test_ping.py .                                                                             [100%]

======================================= 2 passed in 0.22s ==================================================

```

All tests were passed - great!
To make different tests, there is a good sample such as [Given-When-Then](https://docs.behat.org/en/v2.5/guides/1.gherkin.html).
The structure consists of 3 non-formal comments to distinguish the code by the logical blocks:

1. _Given_: preconditions, some known state before the further system/code interactions. 
   It could be manipulations with DB, set the time on specific environment other configurations.
   
2. _When_: interactions with system/code described as steps of Test Cases. 
    Also could be performed with _And_ comment.
   
3. _Then_: outcome observations realised with assertions described as Expected result of Test Case 
   which approve that the code/feature works as expected.
   Could be performed with _And_ comment.
   
In the previous code it would have the next form:

```python
import json
from django.urls import reverse


def test_ping(client):
    # Given -> as a precondition there is an 'url' which is going to be invoked in the next steps
    url = reverse("ping")
    
    # When -> manipulation: get response from given 'url'
    response = client.get(url)
    # And -> manipulation: convert content to the applicable format
    content = json.loads(response.content)
    
    # Then -> check expected result: successful status
    assert response.status_code == 200
    # And -> check expected result: content value
    assert content["ping"] == "pong"

```
