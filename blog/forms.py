from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")  
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']




