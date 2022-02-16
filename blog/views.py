from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
# Create your views here.

class CategoryListView(ListView):
    """Список категорій"""
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'include/category_list.html'



class PostListView(ListView):
    """Список по категоріям. Пости"""
    model = Post
    context_object_name = 'post_list_view'
    template_name = 'blog/post_list.html'



    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))


class PostDetailView(DetailView):
    """Деталі Посту"""
    model = Post
    context_object_name = 'post_detail_view'
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("category"), slug=self.kwargs.get('slug'))





