from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FiedsMixin, FormValidMixin, AuthorAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article
from account.models import User

# Create your views here.
class ArticleList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        
        else:
            return Article.objects.filter(author=self.request.user)
        
        
class ArticleCreate(LoginRequiredMixin, FormValidMixin, FiedsMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin, FormValidMixin, FiedsMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"
    
    
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = "registration/article-delete.html"

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/user-update.html"
    success_url = reverse_lazy("account:home")
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_superuser'
    ]

