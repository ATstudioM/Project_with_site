from django import forms
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