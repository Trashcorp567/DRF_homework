from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import NULLABLE


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='адрес')
    phone = models.CharField(max_length=20, unique=True, verbose_name='номер телефона', **NULLABLE)
    town = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='media/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

