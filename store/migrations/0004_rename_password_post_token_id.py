# Generated by Django 3.2 on 2023-08-19 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='password',
            new_name='token_id',
        ),
    ]
