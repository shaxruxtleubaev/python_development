from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer