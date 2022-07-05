from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListByPageView,
    PostListView,
    PostCreateView,
    PostRetrieveUpdateDestroyView,
    TagListCreateView,
    TagRetrieveUpdateDestroyView,
    CommentCreateView,
    CommentListView,
    CommentRetrieveUpdateDestroyView,
    GetLastFivePostsView,
    GetTagPosts,
    GetPostComments,
    PostListByUserView,
    UpdateAvatarProfileView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('post/list/', PostListByPageView.as_view(), name='post-list'),
    path('post/list/all/', PostListView.as_view(), name='post-all'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/detail/<slug:slug>', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('aside/', GetLastFivePostsView.as_view(), name='aside'),
    path('tag/list', TagListCreateView.as_view(), name='tag-create-and-list'),
    path('tag/detail/<slug:slug>', TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
    path('comment/list/', CommentListView.as_view(), name='comment-list'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/detail/<int:pk>', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
    path('tag/<slug:slug>', GetTagPosts.as_view(), name='tag-posts'),
    path('post-comments/<slug:slug>', GetPostComments.as_view(), name='post-comments'),
    path('user-posts/<slug:slug>/', PostListByUserView.as_view(), name='user-posts'),
    path('update/avatar/<slug:slug>/', UpdateAvatarProfileView.as_view(), name='update-avatar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
