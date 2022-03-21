from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError


class AddPostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a category"

    class Meta:
        model = Post
        fields = ('name', 'slug', 'description', 'description_cod', 'category', 'is_published')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Team description',
            }),
            'description_cod': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Command code',
            }),

        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('The name exceeds 200 characters')
        return name


class AddCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Category Name"


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category name',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),
        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('The name exceeds 200 characters')
        return name


class UpdatePostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a category"

    class Meta:
        model = Post
        fields = ('name', 'slug', 'description', 'description_cod', 'category', 'is_published')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug',

            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description of commands',
            }),
            'description_cod': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Command code',
            }),

        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('The name exceeds 200 characters')
        return name


class AddCommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please provide a comment',
            }),
        }





