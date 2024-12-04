from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from .models import *

class SearchForm(forms.Form):
    text = forms.CharField(label="", max_length=256, widget=forms.TextInput(attrs={"class": "form-control form-control-dark text-bg-dark", 
                                                                                   "type": "search",
                                                                                   "placeholder": "Поиск...",
                                                                                   "aria-label": "Search"}), required=False)

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control form_input', 'placeholder': "Имя пользователя"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control form_input', 'placeholder': "Email"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form_input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form_input', 'placeholder': "Подтверждение пароля"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control form_input', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form_input', 'placeholder': 'Пароль'}))


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone_number', 'birth_date']
        widgets = {
            'birth_date' : AdminDateWidget(attrs = {"type" : "date"}, format = "%Y-%m-%d"),
        }