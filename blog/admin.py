from django.contrib import admin
from .models import Post
from .models import Comment, Post
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
 