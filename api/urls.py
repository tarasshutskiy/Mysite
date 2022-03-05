from django.urls import path
from . import views


urlpatterns = [

    path('v1/postlist/', views.PostAPIView.as_view(), name='api'),
]
