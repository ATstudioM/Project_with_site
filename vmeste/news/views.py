from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

# Create your views here.

menu = [{'title': "О сайте",
         'url_name': 'about'},
        {'title': "Добавить статью",
         'url_name': 'add_news'},
        {'title': "Войти",
         'url_name': 'login'}
]


def index(request):
    posts = News.objects.all()
    tags = {'posts': posts,
            'menu': menu,
            'title': 'Главная страница',
            'cat_selected': 0}
    return render(request, 'news/index.html', context=tags)

def show_news(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'news/post.html', context=context)

def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})


def new(request, newsid):
    if str(newsid) == 'Bubble':
        return redirect('https://bubble.ru/')


def add_news(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                News.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
#БЕДЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ
    else:
        form = AddPost()
    return render(request, 'news/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление поста'})


def login(request):
    return HttpResponse('Типо регистрация')


def pageNotFound(requests, exception):
    return HttpResponseNotFound('<p>Страница не найдена</p>')


def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    tags = {'posts': posts,
            'menu': menu,
            'title': 'Тема',
            'cat_selected': cat_id}
    return render(request, 'news/index.html', context=tags)
