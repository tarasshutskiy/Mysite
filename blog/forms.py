from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'