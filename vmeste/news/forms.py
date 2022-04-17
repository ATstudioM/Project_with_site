from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Нет темы'


    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 20})
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина больше 200 символов (￢_￢;)')

        return title


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Имя/Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Пароль ещё раз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginingUser(AuthenticationForm):
    username = forms.CharField(label='Имя/Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

