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
