from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from blog.forms import RegisterUserForm, LoginForm
from blog.utils import DataMixin




class Registration (CreateView):
    form_class = RegisterUserForm
    template_name = 'autreg.html'
    success_url = reverse_lazy('authorization')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['title_form_btn'] = 'Зарегистрироваться'
        context['link'] = 'aut'
        context['text_help'] = 'Уже есть аккаунт ?'
        context['text_help2'] = 'Авторизуйтесь'
        return context

class Authorization (LoginView):
    form_class = LoginForm
    template_name = "autreg.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['title_form_btn'] = 'Авторизоваться'
        context['link'] = 'reg'
        context['text_help'] = 'Нет аккаунта ?'
        context['text_help2'] = 'Зарегистрируйтесь'

        return context
def index (request):
    context = {
        'title' : 'Блог'
    }
    return render(request , 'autreg.html' , context=context)

# Create your views here.
