from django.urls import path
from . import views


urlpatterns = [



    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

    path('new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),




]
