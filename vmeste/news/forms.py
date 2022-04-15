from django import forms
from .models import *

class AddPost(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
