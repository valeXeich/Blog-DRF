from rest_framework import permissions, generics, pagination, filters
from rest_framework.parsers import MultiPartParser

from .models import Post, Tag, Comment, Profile
from .serializers import PostSerializer, PostCreateSerializer, TagSerializer, CommentSerializer, CommentCreateSerializer, ProfileSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    ordering = '-created_date'


class PaginationForProfile(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    ordering = '-created_date'


class PostListByPageView(generics.ListAPIView):
    """"
    View to get a list of posts
    """
    search_fields = ['content', 'title']
    filter_backends = (filters.SearchFilter, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostListByUserView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    pagination_class = PaginationForProfile

    def get_queryset(self):
        username = self.kwargs['slug']
        posts = Post.objects.filter(author__username=username)
        return posts


class PostCreateView(generics.CreateAPIView):
    """"
    View to create a post
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        tags = self.request.data['tags_pk']
        return serializer.save(author=self.request.user, tags=tags)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """"
    View to get a detail, update, delete post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'


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
    lookup_field = 'slug'
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]


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
        data = self.request.data
        post_slug = data['post']
        post = Post.objects.get(slug=post_slug)
        return serializer.save(author=self.request.user, post=post)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """"
    View to get a detail, update, delete comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class GetLastFivePostsView(generics.ListAPIView):
    queryset = Post.objects.order_by('-created_date')[:5]
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class GetTagPosts(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination

    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=tag_slug)
        posts = Post.objects.filter(tags=tag)
        return posts


class GetPostComments(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        post_slug = self.kwargs['slug']
        comments = Comment.objects.filter(post__slug=post_slug)
        return comments


class UpdateAvatarProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser]
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



