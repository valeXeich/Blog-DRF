from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='user_avatar/', null=True, blank=True)

    def __str__(self):
        return self.user


class Tag(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=255)
    content = models.TextField('Текст')
    poster = models.ImageField('Постер', upload_to='poster/')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    update_date = models.DateTimeField('Редактирован', auto_now=True)
    created_date = models.DateTimeField('Создан', auto_now_add=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    created_date = models.DateTimeField('Создан', auto_now_add=True)
    content = models.TextField('Текст')
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)


