import secrets
import string

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'country', 'phone_number', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


def generate_password(request):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(16))  # генерируем пароль длиной 16 символов
    request.user.set_password(password)

    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {password}!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))
