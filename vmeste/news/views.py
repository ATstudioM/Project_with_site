from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

menu = ['О сайте', 'Добавить статью', 'Войти']


def index(request):
    posts = News.objects.all()
    tags = {'posts': posts, 'menu': menu, 'title': 'Главная страница'}
    return render(request, 'news/index.html', context=tags)

def show_news(request, post_id):
    return HttpResponse(f'Статейка с айди = {post_id}')

def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})


def new(request, newsid):
    if str(newsid) == 'Bubble':
        return redirect('https://bubble.ru/')


def add_news(request):
    return HttpResponse('Добавлние статьи')


def login(request):
    return HttpResponse('Типо регистрация')



def pageNotFound(requests, exception):
    return HttpResponseNotFound('<p>Страница не найдена</p>')
