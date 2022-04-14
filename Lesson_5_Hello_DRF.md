### Hello DRF

Django REST Framework has own components of DB:
1. [_Serializers_](https://www.django-rest-framework.org/api-guide/serializers/): for converting the models instances (requests to DB) to JSON([serialize](https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects)) or vice versa ([deserialize](https://www.django-rest-framework.org/api-guide/serializers/#deserializing-objects)).
2. [_ViewSets_](https://www.django-rest-framework.org/api-guide/viewsets/): similar to Django views, except that automatic responses for GET, POST etc.
the models that are used, and the way of the serialized result data (Serializers).

Let's create the model or table in the DB to manage the books.<br>
First, create the [test](tests/books/test_create_model.py) to make sure that they are created as we expect.<br>

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
        year="2022",
        author="Andros Fenollosa",
    )
    book.save()

    ## When

    ## Then
    assert book.title == "Real-time-Django"
    assert book.genre == "Technical"
    assert book.year == "2022"
    assert book.author == "Andros Fenollosa"
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title
```

And create the [model](books/models.py) for the test:

```python
# books/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
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

The test passed without any problem. 