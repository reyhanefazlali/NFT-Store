# Generated by Django 3.2 on 2023-08-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_create_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='discription',
            field=models.TextField(),
        ),
    ]
