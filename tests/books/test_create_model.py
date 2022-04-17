import pytest

from books.models import Books


@pytest.mark.django_db
def test_books_model():
    book = Books(
        title="Real-time-Django",
        genre="Technical",
        year=2022,
        author="Andros Fenollosa",
    )
    book.save()

    assert book.title == "Real-time-Django"
    assert book.genre == "Technical"
    assert book.year == 2022
    assert book.author == "Andros Fenollosa"
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title
