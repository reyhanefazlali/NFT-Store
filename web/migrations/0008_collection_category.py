# Generated by Django 3.2 on 2023-08-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='category',
            field=models.ManyToManyField(to='web.Category'),
        ),
    ]
