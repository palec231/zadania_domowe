from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Dealer, Car

# Register your models here.
# admin.site.register(Car)   # Zadanie 1


class CarInLine(admin.TabularInline):
    model = Car
    extra = 1  
    
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    inlines = [CarInLine]  # Możesz dodać CarInline, jeśli chcesz zarządzać samochodami bezpośrednio z poziomu dealera       

@admin.register(Car)  # Zadanie 2
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'full_name', 'year', 'is_available', 'photo_thumbnail') # Zadanie 2 i 6
    search_fields = ('brand', 'model') # Zadanie 3
    list_filter = ('is_available', 'year') # Zadanie 4
    ordering = ('-year',) # Zadanie 5
    actions = ['mark_as_unavailable'] # Zadanie 8
    
    # Zadanie 6
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    full_name.short_description = 'Pełna nazwa'

    # Zadanie 7   readonly_fields = ('year',)
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ("year",)
        return ()

        # Zadanie 8
    def mark_as_unavailable(self, request, queryset):
        rows_updated = queryset.update(is_available=False)
        self.message_user(request, f"{rows_updated} samochodów oznaczono jako niedostępne.", messages.SUCCESS)

    mark_as_unavailable.short_description = "Oznacz jako niedostępne"

        #Zadanie 9
    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "Brak zdjęcia"
    
    photo_thumbnail.short_description = 'Miniatura'