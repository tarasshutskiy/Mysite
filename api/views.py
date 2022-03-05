# rest_framework
from rest_framework import generics

from api.serializers import PostSerializer
from blog.models import Post


class PostAPIView(generics.ListAPIView):
    """АПІ"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
