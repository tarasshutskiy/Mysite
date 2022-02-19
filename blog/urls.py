from django.urls import path
from . import views


urlpatterns = [

    path('', views.CategoryListView.as_view(), name='category_list'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),




]
