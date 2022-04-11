from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_news/', add_news, name='add_news'),
    path('login/', login, name='login'),
    path('news/<int:post_id>/', show_news, name='news')
]
