"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path(
        "accounts/logout/success/",
        TemplateView.as_view(template_name="account/logout_success.html"),
        name="logout_success"
    ),
]

handler404 = 'blog.views.handler404'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
