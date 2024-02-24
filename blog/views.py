from typing import Any, Dict
from django.db.models.query import QuerySet
from account.models import User
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.

# def home(request, page=1):
#     articels_list = Article.objects.published()
#     paginator = Paginator(articels_list, 6)
#     articels = paginator.get_page(page)
    
#     context = {
#         "articels" : articels,
#     }
#     return render(request, "blog/home.html", context)



class ArticleList(ListView):
    # model = Article
    # template_name = "blog/home.html"
    context_object_name = "articels"
    queryset = Article.objects.published()
    paginate_by = 6

# def detail(request, slug):
#     context = {
#         "article" : get_object_or_404(Article.objects.published(), slug=slug),
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDelete(DeleteView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
    template_name = "blog/article_delete.html"
    
# def category(request, slug, page=2):
#     category =  get_object_or_404(Category, slug=slug, status=True)
#     articels_list = category.articels.published()
#     paginator = Paginator(articels_list, 6)
#     articels = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articels": articels,
#     }
#     return render(request, "blog/category.html", context)


class CategoryList(ListView):
    paginate_by = 5
    template_name = "blog/category_list.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articels.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    

class AuthorList(ListView):
    paginate_by = 5
    template_name = "blog/author_list.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articels.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context