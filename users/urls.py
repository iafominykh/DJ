from django.urls import path

from users.apps import UsersConfig
from users.forms import generate_password
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_password, name='generate_password'),
]
