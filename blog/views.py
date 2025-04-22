from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm 


def post_list(request):
    post_list = Post.objects.all()  
    paginator = Paginator(post_list, 3)  # 3 posts per page

    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)  # Handles out-of-range pages

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # don't save to DB yet
            post.author = request.user      # assign the logged-in user as the author
            post.save()  
            messages.success(request, "Post created successfully!")                    
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

from django.shortcuts import redirect

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted!")
        return redirect('post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.user != post.author:
        return HttpResponseForbidden()
