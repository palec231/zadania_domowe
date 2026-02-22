from django.contrib import admin
from .models import Article, Category # Importujemy nasz model

# Register your models here.

admin.site.register(Article) # Rejestrujemy model 
admin.site.register(Category) # Rejestrujemy model