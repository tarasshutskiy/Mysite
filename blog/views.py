
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import AddPostForm, AddCategoryForm, UpdatePostForm
from .models import Post, Category
# Create your views here.


class PostListView(ListView):
    """ Пости"""
    model = Post
    paginate_by = 6
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'
    ordering = ['name']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            post_list = Post.objects.filter(name__icontains=query)
            return post_list
        else:
            post_list = Post.objects.all()
            return post_list


class PostDetailView(DetailView):
    """Деталі Посту"""
    model = Post
    context_object_name = 'post_detail'
    slug_url_kwarg = 'slug'
    template_name = 'post/post_detail.html'


class PostCreateView(CreateView):
    """Створити Посту"""
    model = Post
    form_class = AddPostForm
    context_object_name = 'post_create'
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    """Оновити Посту"""
    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post_edit.html'
    context_object_name = 'post_edit'
    slug_url_kwarg = 'slug'


class PostDeleteView(DeleteView):
    """Видалити Посту"""
    model = Post
    context_object_name = 'post_delete'
    template_name = 'post/post_delete.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('post_list')


class CategoryCreateView(CreateView):
    """Створити Категорію"""
    model = Category
    form_class = AddCategoryForm
    context_object_name = 'category_create'
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('post_list')


class CategoryView(ListView):
    """Список категорій"""
    model = Post
    paginate_by = 6
    context_object_name = 'category'
    template_name = 'category/categories.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['cat_slug']).order_by('name')
















