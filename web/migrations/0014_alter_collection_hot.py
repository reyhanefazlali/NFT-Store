# Generated by Django 3.2 on 2023-08-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_collection_hot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='hot',
            field=models.BooleanField(default=True),
        ),
    ]