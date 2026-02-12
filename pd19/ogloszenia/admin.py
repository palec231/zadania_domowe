from django.contrib import admin
from .models import Ogloszenie # Importujemy nasz model

# Register your models here.

class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ("tytul", "cena", "data_dodania")

admin.site.register(Ogloszenie, OgloszenieAdmin) # Rejestrujemy modele