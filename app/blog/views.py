from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView , View , ListView

from blog.forms import RegisterUserForm, LoginForm
from blog.models import *
from blog.utils import DataMixin

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

class Post_detail(View):
    def get(self , request , slug):
        pass
class Posts_by_category(ListView):
    model = Artwork
    template_name = 'blog/index.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Artwork.objects.filter(category__slug=self.kwargs["slug_category"])


# Страница самого поста
# def post_view(request, slug):
#     post = Post.objects.get(slug=slug)
#
#     ip = get_client_ip(request)
#
#     if Ip.objects.filter(ip=ip).exists():
#         post.views.add(Ip.objects.get(ip=ip))
#     else:
#         Ip.objects.create(ip=ip)
#         post.views.add(Ip.objects.get(ip=ip))
#
#     context = {
#         'post': post,
#     }
#     return render(request, 'main/post.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
def index (request):
    context = {
        # 'title' : 'Блог'
    }
    return render(request , 'blog/index.html' , context=context)


class Registration (CreateView):
    form_class = RegisterUserForm
    template_name = 'autreg.html'
    success_url = reverse_lazy('aut')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['title_form'] = 'Регистрация'
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
        context['title_form'] = 'Авторизоваться'
        context['title_form_btn'] = 'Авторизоваться'
        context['link'] = 'reg'
        context['text_help'] = 'Нет аккаунта ?'
        context['text_help2'] = 'Зарегистрируйтесь'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


