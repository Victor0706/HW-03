from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm, ProfileUserForm, LoginUserForm
from messenger import settings


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def profile(request):
    return render(request, 'profile.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('profile')
    extra_context = {'title':'Регистрация'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileList(ListView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile_list.html'
    context_object_name = 'users'
    paginate_by = 8


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('profile')








