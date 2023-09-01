# Generated by Django 3.2 on 2023-08-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20230821_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='posts',
        ),
        migrations.AddField(
            model_name='author',
            name='posts',
            field=models.ManyToManyField(to='store.Post'),
        ),
    ]