# -*- coding: utf-8 -*-
from models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse

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
