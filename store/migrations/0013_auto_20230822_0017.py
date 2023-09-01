# Generated by Django 3.2 on 2023-08-21 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0012_auto_20230821_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='username',
        ),
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
