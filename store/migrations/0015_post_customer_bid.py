# Generated by Django 3.2 on 2023-08-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20230822_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='customer_bid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
