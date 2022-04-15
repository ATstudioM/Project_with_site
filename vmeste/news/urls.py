from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_news/', add_news, name='add_news'),
    path('login/', login, name='login'),
    path('news/<slug:post_slug>/', show_news, name='news'),
    path('category/<int:cat_id>/', show_category, name='category')
]
