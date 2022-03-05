from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Логін',
            }),
            'email': EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль',

            }),

            'password2': PasswordInput(attrs={
                'class': 'form-input',
            }),

        }


