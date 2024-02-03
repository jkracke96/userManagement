from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
import os


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'main/home.html', {"posts": posts})


@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # don't commit to DB yet because author is not specified
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm

    return render(request, "content/create_post.html", {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


class MyPasswordResetView(PasswordResetView):
    from_email = str(os.getenv('EMAIL_USER'))

