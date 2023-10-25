from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='manager@gmail.com',
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('123qwe456rty')
        user.save()
