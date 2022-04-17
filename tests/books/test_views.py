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
    resp = client.get(f"/books/11/")
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

@pytest.mark.django_db
def test_remove_book(client):

    book = Books.objects.create(
        title=book_detail["title"],
        genre=book_detail["genre"],
        author=book_detail["author"],
        year=book_detail["year"],
    )

    response_detail = client.get(f"/books/{book.id}/")
    assert response_detail.status_code == 200
    assert response_detail.data["title"] == book_detail["title"]

    response_delete = client.delete(f"/books/{book.id}/")
    response_list = client.get("/books/")
    response_new_detail = client.get(f"/books/{book.id}/")

    assert response_delete.status_code == 200
    assert response_delete.data["title"] == book_detail["title"]
    assert response_list.status_code == 200
    assert len(response_list.data) == 0
    assert response_new_detail.status_code == 404

@pytest.mark.django_db
def test_remove_invalid_book_id(client):
    book = Books.objects.create(
        title=book_detail["title"],
        genre=book_detail["genre"],
        author=book_detail["author"],
        year=book_detail["year"],
    )

    resp = client.delete("/books/11/")
    assert resp.status_code == 404
