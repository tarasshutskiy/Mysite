from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError

class AddPostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Автор"
        self.fields['category'].empty_label = "Виберіть категорію"


    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва посту',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описання команди',
            }),
            'description_cod': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Код команди',
            }),

        }



    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Назва перевищує 200 символів')
        return name


class AddCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Назва Категорії"


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва категорії',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),
        }



    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Назва перевищує 200 символів')
        return name



class UpdatePostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Автор"
        self.fields['category'].empty_label = "Виберіть категорію"

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва посту',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описання команди',
            }),
            'description_cod': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Код команди',
            }),

        }



    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Назва перевищує 200 символів')
        return name
