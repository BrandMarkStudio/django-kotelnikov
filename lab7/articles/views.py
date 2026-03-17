# -*- coding: utf-8 -*-
from models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Проверка на пустые поля
        if not username or not password:
            return render(request, 'login.html', {
                'error': u"Пожалуйста, заполните все поля"
            })

        # Аутентификация
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # после успешного входа → главная страница
        else:
            return render(request, 'login.html', {
                'error': u"Нет аккаунта с таким сочетанием никнейма и пароля"
            })
    else:
        # GET-запрос: просто показать форму входа
        return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        # Получаем данные из формы
        form = {
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', '')
        }

        # Проверка, что все поля заполнены
        if not form['username'] or not form['email'] or not form['password']:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})

        # Проверка уникальности имени пользователя
        if User.objects.filter(username=form['username']).exists():
            form['errors'] = u"Пользователь с таким именем уже существует"
            return render(request, 'registration.html', {'form': form})

        # Создаем нового пользователя
        user = User.objects.create_user(
            username=form['username'],
            email=form['email'],
            password=form['password']
        )
        return redirect('/')  # после регистрации можно на главную или страницу входа
    else:
        # GET-запрос: показать пустую форму
        return render(request, 'registration.html', {'form': {}})

def create_post(request):
    if request.method == "POST":
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }

        # проверка, что поля заполнены
        if not form['title'] or not form['text']:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        # проверка уникальности заголовка
        if Article.objects.filter(title=form['title']).exists():
            form['errors'] = u"Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        # создать статью
        post = Article.objects.create(
            title=form['title'],
            text=form['text'],
            author=request.user
        )
        return redirect('get_article', article_id=post.id)

    else:
        return render(request, 'create_post.html', {'form': {}})

def archive(request):
    return render(request, 'archive.html', {"posts":Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
