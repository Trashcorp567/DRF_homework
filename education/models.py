from django.db import models

from config import settings

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    active_sub = models.BooleanField(default=False, verbose_name='статус подписки')

    def __str__(self):
        return f'{self.user, self.course, self.active_sub}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

