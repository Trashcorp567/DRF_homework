from django.db import models
from django.utils import timezone

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    name = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='media/', verbose_name='превью ', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    cost = models.IntegerField(default=0, verbose_name='цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name',)


class Lesson(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    name = models.CharField(max_length=150, verbose_name='название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    image = models.ImageField(upload_to='media/', verbose_name='превью ', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    start_date = models.DateTimeField(verbose_name='дата подписки', default=timezone.now)
    is_subscribed = models.BooleanField(verbose_name='статус', default=True)
    email = models.EmailField(verbose_name='почта', **NULLABLE)

    def __str__(self):
        return f'{self.user}{self.course}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
