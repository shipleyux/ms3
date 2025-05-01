# blog/forms.py
#
# This file defines forms for creating posts, submitting comments, and registering new users.


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from .models import Post, Category
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'email' in self.fields:
            del self.fields['email']

        self.fields['username'].label = "Username"
        self.fields['username'].help_text = "Usernames must not contain spaces."
        self.fields['username'].required = True

    def save(self, request):
        user = super().save(request)
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


