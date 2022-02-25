from django.urls import path
from . import views


urlpatterns = [


    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:category_slug>/', views.CategoryListView.as_view(), name='category'),
    path('<slug:post_slug>/', views.PostDetailView.as_view(), name='post'),



    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('<slug:post_slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<slug:post_slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),




]
