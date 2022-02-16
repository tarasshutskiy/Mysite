from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list_view'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_view'),


]
