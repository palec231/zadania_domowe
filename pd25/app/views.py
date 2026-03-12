from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Note, Author, Book 
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer 
from django.http import HttpResponse
from rest_framework.decorators import api_view # Zadanie 7
from rest_framework.response import Response # Zadanie 7
from rest_framework import status # Zadanie 7

# zadanie 3
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Zadanie 8
    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

# Zadanie 4 
# Dodano w Postmanie 3 produkty przy użyciu POST
# Metoda GET "http://127.0.0.1:8000/api/products/" zwróciła:
# [
#     {
#         "id": 1,
#         "name": "Produkt 1",
#         "price": "20.50"
#     },
#     {
#         "id": 2,
#         "name": "Produkt 2",
#         "price": "28.50"
#     },
#     {
#         "id": 3,
#         "name": "Produkt 3",
#         "price": "31.20"
#     }
# ]

# Zadanie 5
def set_name(request):
    name = request.GET.get("name")
    response = HttpResponse(f"Ustawiono imię: {name}" if name else "Nie podano imienia.")
    if name:
        response.set_cookie("user_name", name)
    return response

def hello(request):
    name = request.COOKIES.get("user_name")
    if name:
        return HttpResponse(f"Witaj, {name}!")
    return HttpResponse("Witaj, Gość!")

# zadanie 6
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

# Zadanie 7
@api_view(["GET"])
def calculate(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operation = request.GET.get("operation")

    if num1 is None or num2 is None or operation is None:
        return Response(
            {"error": "Parametry num1, num2 i operation są wymagane."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return Response(
            {"error": "Parametry num1 i num2 muszą być liczbami."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return Response(
                {"error": "Nie można dzielić przez zero."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = num1 / num2
    else:
        return Response(
            {"error": "Niepoprawna operacja. Dozwolone: add, subtract, multiply, divide."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response({"result": result}, status=status.HTTP_200_OK)

# Zadanie 9
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer