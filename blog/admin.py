from django.contrib import admin

# Register models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
