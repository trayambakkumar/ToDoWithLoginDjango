from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, AddForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    form = AddForm()
    if request.user.is_authenticated:
        user = request.user
        posts = user.post_set.all()
        return render(request, "ToDo/home.html", {'form': form, 'posts': posts})
    else:
        return render(request, "ToDo/home.html", {'form': form})


@login_required
def add(request):
    form = AddForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data.get('text')
        user = request.user
        post = Post.objects.create(user=user, text=text)
        post.save()
    return redirect('home')


def delete(request, key_id):
    post = Post.objects.get(id=key_id)
    post.delete()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, "ToDo/signup.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            try:
                auth_login(request, user)
            except:
                form = LoginForm()
                return render(request, "ToDo/login.html", {'form': form})
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, "ToDo/login.html", {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')


