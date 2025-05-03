# blog/urls.py
#
# This file maps URL patterns to the corresponding view functions
# for the blog application.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path(
        'category/<int:category_id>/',
        views.posts_by_category,
        name='posts_by_category'
    ),
    path(
        'comment/<int:pk>/edit/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'comment/<int:pk>/delete/',
        views.delete_comment,
        name='delete_comment'
    ),
]

handler404 = 'blog.views.handler404'



