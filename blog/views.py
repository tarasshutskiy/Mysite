from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import AddPostForm, AddCategoryForm
from .models import Post, Category
# Create your views here.

class CategoryListView(ListView):
    """Список категорій"""
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category_list'
    template_name = 'category/category_list.html'



class PostListView(ListView):
    """Список по категоріям. Пости"""
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'



    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))


class PostDetailView(DetailView):
    """Деталі Посту"""
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post/post_detail.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("category"), slug=self.kwargs.get('slug'))



class PostCreateView(CreateView):
    """Створити Посту"""
    form_class = AddPostForm
    context_object_name = 'post_create'
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('category_list')



class CategoryCreateView(CreateView):
    """Створити Посту"""
    form_class = AddCategoryForm
    context_object_name = 'category_create'
    template_name = 'category/category_create.html'

