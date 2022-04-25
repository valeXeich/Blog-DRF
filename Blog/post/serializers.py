from rest_framework import serializers
from .models import Post, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'content', 'post']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    slug = serializers.SlugField(required=False, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ['status']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'author']
        read_only_fields = ['author']

