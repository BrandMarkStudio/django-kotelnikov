# -*- coding: utf-8 -*-
from models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    next_url = request.GET.get('next', request.POST.get('next', '/'))

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'login.html', {
                'error': u"Пожалуйста, заполните все поля",
                'next': next_url,
            })

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, 'login.html', {
                'error': u"Нет аккаунта с таким сочетанием никнейма и пароля",
                'next': next_url,
            })

    return render(request, 'login.html', {'next': next_url})


def user_logout(request):
    logout(request)
    return redirect('/')


def registration(request):
    next_url = request.GET.get('next', request.POST.get('next', '/'))

    if request.method == "POST":
        form = {
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', '')
        }

        if not form['username'] or not form['email'] or not form['password']:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form, 'next': next_url})

        if User.objects.filter(username=form['username']).exists():
            form['errors'] = u"Пользователь с таким именем уже существует"
            return render(request, 'registration.html', {'form': form, 'next': next_url})

        User.objects.create_user(
            username=form['username'],
            email=form['email'],
            password=form['password']
        )

        user = authenticate(username=form['username'], password=form['password'])
        if user is not None:
            login(request, user)

        return redirect(next_url)

    return render(request, 'registration.html', {'form': {}, 'next': next_url})


def create_post(request):
    if request.user.is_anonymous():
        return redirect('/login/?next=/article/new/')

    if request.method == "POST":
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }

        if not form['title'] or not form['text']:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        if Article.objects.filter(title=form['title']).exists():
            form['errors'] = u"Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        post = Article.objects.create(
            title=form['title'],
            text=form['text'],
            author=request.user
        )
        return redirect('get_article', article_id=post.id)

    return render(request, 'create_post.html', {'form': {}})


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
