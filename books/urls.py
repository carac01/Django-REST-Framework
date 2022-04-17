from django.urls import path
from books.views import ping, BooksList, BookDetails

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("books/", BooksList.as_view()),
    path("books/<int:pk>/", BookDetails.as_view()),
]
