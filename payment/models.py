from django.db import models

from config import settings
from education.models import Lesson, Course, NULLABLE


# Create your models here.
class Payment(models.Model):
    payment_choice = [('cash', 'Наличные'), ('bank_transfer', 'Перевод на счет')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='время платежа', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    paid_cost = models.PositiveIntegerField(default=0, verbose_name='Стоимость оплаты', **NULLABLE)
    pay_method = models.CharField(max_length=25, choices=payment_choice, verbose_name='способ оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user, self.pay_method, self.paid_cost, self.payment_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
