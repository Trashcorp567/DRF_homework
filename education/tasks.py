from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from education.models import Subscription


@shared_task
def send_mailing_update(pk, model):
    send_mail(
        subject=f'Обновление курса {model}',
        message='Курс обновился',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[pk]
    )

@shared_task
def send_mailing_create(pk, model):
    send_mail(
        subject='Создание курса',
        message=f'Вы создали курс{model.name}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[pk]
    )