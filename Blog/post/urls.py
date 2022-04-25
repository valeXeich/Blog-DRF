from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListView,
    PostCreateView,
    PostRetrieveUpdateDestroyView,
    TagListCreateView,
    TagRetrieveUpdateDestroyView,
    CommentCreateView,
    CommentListView,
    CommentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('post/list', PostListView.as_view(), name='post-list'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/detail/<int:pk>', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('tag/list', TagListCreateView.as_view(), name='tag-create-and-list'),
    path('tag/detail/<int:pk>', TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
    path('comment/list', CommentListView.as_view(), name='comment-list'),
    path('comment/create', CommentCreateView.as_view(), name='comment-create'),
    path('comment/detail/<int:pk>', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)