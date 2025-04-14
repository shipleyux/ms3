"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include  #  include here to handle other app URLs
from blog.views import post_list  #  main view for the home page

urlpatterns = [
    path('', post_list, name='home'),  # Home page that uses the post_list view
    path('admin/', admin.site.urls),  # Admin URL
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for login, registration, etc.
]

