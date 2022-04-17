### Delete

Now let's give the possibility to delete the book.
We will edit the tests for views module to check that the book is removed as expected - 
and if we delete not existed book, we will get expected error code.

```python
...
book_detail = {
        "title": "Real-time-Django",
        "genre": "Technical",
        "author": "Andros Fenollosa",
        "year": 2022,
}

...

@pytest.mark.django_db
def test_remove_book(client): # new

    # Given
    book = Books.objects.create(
        title=book_detail["title"],
        genre=book_detail["genre"],
        author=book_detail["author"],
        year=book_detail["year"],
    )
    ## Check exist
    response_detail = client.get(f"/books/{book.id}/")
    assert response_detail.status_code == 200
    assert response_detail.data["title"] == book_detail["title"]

    # When
    response_delete = client.delete(f"/books/{book.id}/")
    response_list = client.get("/books/")
    response_new_detail = client.get(f"/books/{book.id}/")

    # Then
    ## Check status delete
    assert response_delete.status_code == 200
    ## Check return delete
    assert response_delete.data["title"] == "El fin de la eternidad"
    ## Check status list
    assert response_list.status_code == 200
    ## Check not item list
    assert len(response_list.data) == 0
    ## Check not exist detail
    assert response_new_detail.status_code == 404

@pytest.mark.django_db
def test_remove_invalid_book_id(client): # new
    # Given
    book = Books.objects.create(
        title=book_detail["title"],
        genre=book_detail["genre"],
        author=book_detail["author"],
        year=book_detail["year"],
    )

    # When
    resp = client.delete("/books/11/")

    # Then
    assert resp.status_code == 404
```

Add the view which is removed the book in [BookDetails](books/views.py).

```python
def delete(self, request, pk): # new
    book = Books.objects.filter(pk=pk).first()
    if book:
        serializer = BookSerializer(book)
        book.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
```