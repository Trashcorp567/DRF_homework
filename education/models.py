from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    name = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to='media/', verbose_name='превью ', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

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


class Payment(models.Model):
    payment_choice = [('cash', 'Наличные'), ('bank_transfer', 'Перевод на счет')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='время платежа', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    paid_cost = models.PositiveIntegerField(verbose_name='стоимость')
    pay_method = models.CharField(max_length=25, choices=payment_choice, verbose_name='способ оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user, self.pay_method, self.paid_cost, self.payment_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    active_sub = models.BooleanField(default=False, verbose_name='статус подписки')

    def __str__(self):
        return f'{self.user, self.course, self.active_sub}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

