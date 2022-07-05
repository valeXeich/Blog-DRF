from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from slugify import slugify


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', default='static/user_avatar/default_avatar.png', upload_to='user_avatar/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=255)
    content = models.TextField('Текст')
    poster = models.ImageField('Постер', upload_to='poster/', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, related_name='posts')
    update_date = models.DateTimeField('Редактирован', auto_now=True)
    created_date = models.DateTimeField('Создан', auto_now_add=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    created_date = models.DateTimeField('Создан', auto_now_add=True)
    content = models.TextField('Текст')
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Комментарий: {self.author}'


