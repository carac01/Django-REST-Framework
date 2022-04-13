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

