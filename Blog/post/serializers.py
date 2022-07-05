from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Tag, Comment, Profile


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
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ['author', 'content', 'post']
        read_only_fields = ['post']


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
        fields = ['title', 'content', 'tags', 'author', 'poster']
        read_only_fields = ['author']

    def to_internal_value(self, data):
        data['tags_pk'] = [int(pk) for pk in data['tags'].strip('[]').split(',')]
        del data['tags']
        return super().to_internal_value(data)

    def validate(self, data):
        if data['title'] in [post.title for post in Post.objects.all()]:
            raise serializers.ValidationError({'taken': 'Post title already taken'})
        if any(map(str.isdigit, data['title'])):
            raise serializers.ValidationError({'number': 'The title of the post should not contain numbers'})
        if len(data['title']) < 5:
            raise serializers.ValidationError(
                {'title_length': 'The title of the post should not be less than 5 characters long'}
            )
        if len(data['content']) < 50:
            raise serializers.ValidationError(
                {'content_length': 'The title of the post should not be less than 50 characters long'}
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['avatar', 'user']


