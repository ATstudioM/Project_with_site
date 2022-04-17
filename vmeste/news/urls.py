from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsTime.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_news/', AddNews.as_view(), name='add_news'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('news/<slug:post_slug>/', ShowNews.as_view(), name='news'),
    path('category/<slug:cat_slug>/', NewsCategory.as_view(), name='category')
]
