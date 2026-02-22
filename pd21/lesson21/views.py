from django.http import HttpResponse
from .models import Category, Article
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


# zadanie 3
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

# zadanie 5 (w konsoli)
# sport = Category.objects.get(name="Sport")
# print(sport)

# zadanie 6
def category_detail_view(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "category_detail.html", {"category": category})

# zadanie 8 / 10
def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by("-pub_date")
    q = request.GET.get("q")
    if q:
        articles = articles.filter(title__icontains=q)
    return render(request, "article_list.html", { "articles": articles, "q": q })

# zadanie 11
def article_list_pag(request):
    articles = Article.objects.filter(is_published=True).order_by("-pub_date")

    q = request.GET.get("q", "").strip()
    if q:
        articles = articles.filter(title__icontains=q)

    paginator = Paginator(articles, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "article_list_pag.html", {
        "page_obj": page_obj,
        # backward compatibility with template that expects `articles`
        "articles": page_obj,
        "q": q,
    })