import pytest
from django.urls import reverse

from books.models import Books

book_detail = {
        "title": "Real-time-Django",
        "genre": "Technical",
        "author": "Andros Fenollosa",
        "year": 2022,
}

@pytest.mark.django_db
def test_add_book(client):
    books = Books.objects.all()
    assert len(books) == 0

    response = client.post(
        "/books/",
        book_detail,
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.data["title"] == "Real-time-Django"

    books = Books.objects.all()
    assert len(books) == 1

@pytest.mark.django_db
def test_get_single_book(client):
    book = Books.objects.create(
        title=book_detail["title"],
        genre=book_detail["genre"],
        author=book_detail["author"],
        year=book_detail["year"],
    )
    resp = client.get(f"/books/{book.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == book_detail["title"]

@pytest.mark.django_db
def test_get_invalid_single_book_id(client):
    resp = client.get(f"/books/-1/")
    assert resp.status_code == 404

@pytest.mark.django_db
def test_get_all_books(client, faker):

    def create_random_book():
        return Books.objects.create(
            title=faker.name(),
            genre=faker.name_nonbinary(),
            author=faker.name_nonbinary(),
            year=faker.year(),
        )

    book_1 = create_random_book()
    book_2 = create_random_book()

    response = client.get("/books/")

    assert response.status_code == 200
    assert response.data[0] == book_1.title
    assert response.data[1] == book_2.title
