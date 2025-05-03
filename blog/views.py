# blog/views.py
#
# This file contains all view functions for handling blog posts, comments,
# and user registration.

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm


def posts_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'active_category': category,
    })


def post_list(request):
    all_posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    featured_post = all_posts.first()
    post_list = all_posts[1:]

    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'featured_post': featured_post,
        'posts': posts,
        'categories': categories,
        'active_category': None,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to comment.")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Ensure author is always set
            post.save()
            messages.success(request, "Post updated successfully!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


def handler404(request, exception):
    return render(request, '404.html', status=404)


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
