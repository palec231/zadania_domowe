from django.urls import path, include
from rest_framework import routers
from . import views

# Zadanie 3
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="product")

router.register(r'notes', views.NoteViewSet, basename="note")  # Zadanie 6
router.register("authors", views.AuthorViewSet, basename="author") # Zadanie 9
router.register("books", views.BookViewSet, basename="book") # Zadanie 9

urlpatterns = [
    path('api/', include(router.urls)),
    path("api/hello/", views.hello, name="hello"),
    path("api/set-name/", views.set_name, name="set_name"),
    path("api/calculate/", views.calculate, name="calculate"),
]