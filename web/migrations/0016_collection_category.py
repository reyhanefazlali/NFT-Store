# Generated by Django 3.2 on 2023-08-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_collection_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='category',
            field=models.ManyToManyField(to='web.Category'),
        ),
    ]