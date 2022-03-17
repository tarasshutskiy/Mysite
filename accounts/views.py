from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView


from accounts.forms import RegisterUserForm


class RegisterUser(CreateView):
    """Реєстрація користувача"""
    form_class = RegisterUserForm
    # form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('post_list')


class LoginUser(LoginView):
    """Авторизація користувача"""
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('post_list')


def logout_user(reguest):
    logout(reguest)
    return redirect('post_list')


