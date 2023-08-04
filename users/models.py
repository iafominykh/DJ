from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(**NULLABLE,verbose_name='Страна', max_length=150)
    phone_number = models.CharField(**NULLABLE,verbose_name='Номер телефона', max_length=25)
    avatar = models.ImageField(upload_to='users/',verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
