from django.contrib import admin
from .models import Post, Tag, Comment, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag),
admin.site.register(Comment)
admin.site.register(Profile)

