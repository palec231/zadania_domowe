from rest_framework import serializers 
from .models import Product, Note, Author, Book

# Zadanie 2
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

# Zadanie 6
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at']
# Zadanie 10
    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Tytuł notatki musi mieć co najmniej 5 znaków."
            )
        return value

# Zadanie 9
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), 
        source='author', 
        write_only=True
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_id']