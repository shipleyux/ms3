# blog/forms.py
#
# forms for creating posts, submitting comments, and registering new users.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'email' in self.fields:
            del self.fields['email']

        self.fields['username'].label = "Username"
        self.fields['username'].help_text = (
            "Usernames must not contain spaces."
        )
        self.fields['username'].required = True

    def save(self, request):
        user = super().save(request)
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Write your post content here...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'category': 'Category',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Your Comment',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment here...',
                'class': 'form-control',
            })
        }

