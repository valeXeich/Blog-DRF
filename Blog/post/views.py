from rest_framework import permissions, generics

from .models import Post, Tag, Comment
from .serializers import PostSerializer, PostCreateSerializer, TagSerializer, CommentSerializer, CommentCreateSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class PostListView(generics.ListAPIView):
    """"
    View to get a list of posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostCreateView(generics.CreateAPIView):
    """"
    View to create a post
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """"
    View to get a detail, update, delete post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TagListCreateView(generics.ListCreateAPIView):
    """"
    View to create and list tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """"
    View to get a detail, update, delete tag
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


class CommentListView(generics.ListAPIView):
    """"
    View to get a list of comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


class CommentCreateView(generics.CreateAPIView):
    """"
    View to create a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permissions = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """"
    View to get a detail, update, delete comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

