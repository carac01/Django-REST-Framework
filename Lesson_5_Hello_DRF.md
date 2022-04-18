### Hello DRF

Django REST Framework has own components of DB:
1. [_Serializers_](https://www.django-rest-framework.org/api-guide/serializers/): for converting the models instances (requests to DB) to JSON([serialize](https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects)) or vice versa ([deserialize](https://www.django-rest-framework.org/api-guide/serializers/#deserializing-objects)).
2. [_ViewSets_](https://www.django-rest-framework.org/api-guide/viewsets/): similar to Django views, except that automatic responses for GET, POST etc.
the models that are used, and the way of the serialized result data (Serializers).

Let's create the model or table in the DB to manage the books.<br>

#### Test
First, create the [test](tests/books/test_create_model.py) to make sure that they are created as we expect.<br>
The test is marked with [pytest.mark.django_db](https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest-mark-django-db-request-database-access) for requesting DB access:<br>

```python
# tests/books/test_create_model.py

import pytest

from books.models import Books


@pytest.mark.django_db
def test_books_model():

    ## Given
    # Create the new book in DB
    book = Books(
        title="Real-time-Django",
        genre="Technical",
        year=2022,
        author="Andros Fenollosa",
    )
    book.save()

    ## When

    ## Then
    assert book.title == "Real-time-Django"
    assert book.genre == "Technical"
    assert book.year == 2022
    assert book.author == "Andros Fenollosa"
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title
```

#### Model

And create the [model](books/models.py) for the test:

```python
# books/models.py

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

```

Prepare migration:

```commandline
python manage.py makemigrations
python manage.py migrate
```
And execute the test:

```commandline
pytest tests/books/test_create_model.py
```

The test passed without any problem. <br><br>

#### Serializer

Now we are going to define the serializer in order to transform the results in the DB - models - to JSON format.
As usual, let's begin from the [test](tests/books/test_serializers.py):

```python
# tests/books/test_serializers.py

from books.serializers import BookSerializer

def test_valid_book_serializer():
    valid_serializer_data = {
        "title": "Holiday in the Wild",
        "genre": "comedy",
        "year": 2o19,
        "author": "Neal Dobrofsky and Tippi Dobrofsky",
    }
    serializer = BookSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

def test_invalid_book_serializer():
    invalid_serializer_data = {
        "title": "Soy Leyenda",
        "author": "Richard Matheson",
    }
    serializer = BookSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {
        "year": ["This field is required."],
        "genre": ["This field is required."],
    }

```

It will fail, because we did not create the Serializer. 

```commandline
pytest
```

Thanks to the test running in advance we know how should it be structured.
Let's create the [serializer](books/serializers.py):

```python
# books/serializers.py

from rest_framework.serializers import ModelSerializer
from .models import Books


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

```

We indicate to include _all_ fields and separate we may _read only_ fields: id, created_at, updated_at.<br>
Now we already could pass the test. If you want to test only the last one that was realized, 
you could run the test with [flag _-k_](https://docs.pytest.org/en/6.2.x/usage.html) and the file name without _test__ prefix.

```commandline
pytest -k serializers
```
