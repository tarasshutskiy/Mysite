import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, DeletionMixin, FormMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from config import settings
from .forms import AddPostForm, AddCategoryForm, UpdatePostForm, AddCommentForm
from .models import Post, Category, Comment


# Create your views here.


class PostListView(ListView):
    """ Пости"""
    model = Post
    paginate_by = 6
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            post_list = Post.objects.filter(
                name__icontains=query,
                is_published=True).select_related('category', 'author', 'user')
            return post_list
        else:
            post_list = Post.objects.filter(is_published=True).select_related('category').order_by('-time_create')
            return post_list


class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    """Деталі Посту"""
    model = Post
    context_object_name = 'post_detail'
    slug_url_kwarg = 'slug'
    template_name = 'post/post_detail.html'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.get_object().slug})

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    """Створити Посту"""
    model = Post
    form_class = AddPostForm
    context_object_name = 'post_create'
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Оновити Посту"""
    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post_edit.html'
    context_object_name = 'post_edit'
    slug_url_kwarg = 'slug'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class PostDeleteView(LoginRequiredMixin, DeleteView, DeletionMixin):
    """Видалити Посту"""
    model = Post
    context_object_name = 'post_delete'
    template_name = 'post/post_delete.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('post_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


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
        return Post.objects.filter(category__slug=self.kwargs['cat_slug']).order_by('-time_create')



def listing(request):
    contact_list = Comment.objects.all()
    paginator = Paginator(contact_list, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'detail_post.html', {'page_obj': page_obj})