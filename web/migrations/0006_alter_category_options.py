# Generated by Django 3.2 on 2023-08-19 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
