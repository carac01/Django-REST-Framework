### Create

The goal is to create CRUD endpoints (add-read-update-delete) with a book
to read it and manage it with all possible ways.

The first purpose is to define the endpoint to create the new book (_POST_).
We will start to create the [new test](tests/books/test_views.py).

```python
# tests/books/test_views.py

import pytest
from books.models import Books


@pytest.mark.django_db
def test_add_book(client):
    # Given
    books = Books.objects.all()
    assert len(books) == 0

    # When
    response = client.post(
        "/books/",
        {
            "title": "Real-time-Django",
            "genre": "Technical",
            "author": "Andros Fenollosa",
            "year": "2022",
        },
        content_type="application/json"
    )

    # Then
    assert response.status_code == 201
    # And
    assert response.data["title"] == "Real-time-Django"
    # And
    books = Books.objects.all()
    assert len(books) == 1
```

The execution will fail as usual (for more information you could see the [explanation of Andros Fenollosa](https://programadorwebvalencia.com/cursos/testing/tdd/))
Let's actualize the view:

```python
# books/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer

...

class BooksList(APIView):

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)
```
To separate the urls of the different applications let's create the route in [urls.py](books/urls.py) for books.

```python
# books/urls.py

from django.urls import path
from books.views import ping, BooksList

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("books/", BooksList.as_view()),
]
```

Inside the [proyecto/urls.py](proyecto/urls.py) we will call the routes for the admin and books application.

```python
# proyecto/urls.py

from django.contrib import admin
from django.urls import path, include # new

from books.views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    path('', include("books.urls")), # new
]
```

Now the tests will be passed.

```commandline
pytest -k views
```

