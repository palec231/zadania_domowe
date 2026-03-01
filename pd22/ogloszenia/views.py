from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category
# Create your views here.


# Zadanie 2
def category_posts(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'ogloszenia/category_posts.html', {'posts': posts, 'category_name': category.name})

# Zadanie 3
def home(request):
    posts = Post.objects.order_by("-published_date")[:5]  
    return render(request, "ogloszenia/home.html", {"posts": posts})

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(request, 'ogloszenia/search_results.html', {'results': results, 'query': query})

qs = Post.objects.filter(
    Q(title__icontains="django") | Q(content__icontains="django"))