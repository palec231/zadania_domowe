from django.contrib import admin
from .models import Post, Category, Tag # Importujemy nasz model

# Register your models here.
# Krok 3: Rejestracja modelu w pliku blog/admin.py
# Dzięki temu model 'Post' pojawi się w panelu administratora.

#admin.site.register(Post) # Rejestrujemy model
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( "title", "category", "author", "get_tags", "published_date")
    list_filter = ("category", "published_date")
    search_fields = ("title", "content", "category__name")
    ordering = ("-published_date",)
    list_select_related = ("category",)

    @admin.display(description="Tagi")
    def get_tags(self, obj):
        return ", ".join(obj.tags.values_list("name", flat=True))

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")