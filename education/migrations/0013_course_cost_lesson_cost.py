# Generated by Django 4.2.5 on 2023-10-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='цена'),
        ),
    ]
