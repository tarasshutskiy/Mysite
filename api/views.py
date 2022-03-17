# rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import PostSerializer
from blog.models import Post


class PostAPIListView(generics.ListAPIView):
    """АПІ"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


