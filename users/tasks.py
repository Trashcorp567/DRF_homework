import datetime

from celery import shared_task

from users.models import User


@shared_task
def block_user():
    user = User.objects.all()
    if user.last_login >= user.last_login+datetime.timedelta(days=31):
        user.is_active = False