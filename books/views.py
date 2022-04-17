from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Books

def ping(request):
    data = {"ping": "pong"}
    return JsonResponse(data)


class BooksList(APIView):

    def get(self, request):
        books = [book.title for book in Books.objects.all()]
        return Response(books)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):

    def get(self, request, pk):
        book = Books.objects.filter(pk=pk).first()
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        book = Books.objects.filter(pk=pk).first()
        if book:
            serializer = BookSerializer(book)
            book.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
