import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule

schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)

PeriodicTask.objects.create(
    interval=schedule,
    name='Block users',
    task='users.tasks.block_user',
    args=json.dumps(['arg1', 'arg2']),
    kwargs=json.dumps({
        'be_careful': True,
    }),
    expires=datetime.utcnow() + timedelta(seconds=30)
)