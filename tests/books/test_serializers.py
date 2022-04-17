from books.serializers import BookSerializer


def test_valid_book_serializer():
    valid_serializer_data = {
        "title": "Holiday in the Wild",
        "genre": "comedy",
        "year": 2019,
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
