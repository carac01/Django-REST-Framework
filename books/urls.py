from django.urls import path
from books.views import ping, BooksList

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("books/", BooksList.as_view()),
]
