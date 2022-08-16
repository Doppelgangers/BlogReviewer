from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин' , widget=forms.TextInput(attrs={'class' : 'w3-input w3-border w3-round' }))
    password1 = forms.CharField(label='Пороль' , widget=forms.PasswordInput(attrs={'class' : 'w3-input w3-border w3-round' }))
    password2 = forms.CharField(label='Повтор попроля' , widget=forms.PasswordInput(attrs={'class' : 'w3-input w3-border w3-round' } ) )

    class Meta:
        model = User
        fields = ('username' , 'password1' , 'password2')
        widgets = {
            'username'  : forms.TextInput( attrs={'class' : 'w3-input w3-border w3-round' })  ,
            'password1' : forms.PasswordInput( attrs={'class' : 'w3-input w3-border w3-round' })  ,
            'password2' : forms.PasswordInput( attrs={'class' : 'w3-input w3-border w3-round' })

        }

class LoginForm (AuthenticationForm):
    username = forms.CharField(label='Логин' , widget= forms.TextInput(attrs={'class' : 'w3-input w3-border w3-round' }))
    password = forms.CharField(label='Пороль' , widget= forms.PasswordInput(attrs={'class' : 'w3-input w3-border w3-round' }))