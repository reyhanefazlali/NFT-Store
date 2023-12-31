# Generated by Django 3.2 on 2023-08-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('price', models.FloatField()),
                ('benefit', models.CharField(max_length=255)),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('Active', models.BooleanField(default=False)),
            ],
        ),
    ]
