# Generated by Django 3.2 on 2023-08-21 20:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0013_auto_20230822_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='username',
        ),
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
