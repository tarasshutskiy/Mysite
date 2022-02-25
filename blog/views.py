from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import AddPostForm, AddCategoryForm
from .models import Post, Category
# Create your views here.




class PostListView(ListView):
    """ Пости"""
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'






class PostDetailView(DetailView):
    """Деталі Посту"""
    model = Post
    context_object_name = 'posts'
    slug_url_kwarg = 'post_slug'
    template_name = 'post/post_detail.html'


    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs.get('post_slug'))



class CategoryListView(ListView):
    """Список категорій"""
    model = Post
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category/list_category.html'






class PostCreateView(CreateView):
    """Створити Посту"""
    model = Post
    form_class = AddPostForm
    context_object_name = 'post_create'
    template_name = 'post/post_create.html'




class CategoryCreateView(CreateView):
    """Створити Посту"""
    form_class = AddCategoryForm
    context_object_name = 'category_create'
    template_name = 'category/category_create.html'




class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'post/post_edit.html'
    context_object_name = 'post_edit'
    slug_url_kwarg = 'post_slug'






class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post_delete'
    template_name = 'post/post_delete.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('post_list')