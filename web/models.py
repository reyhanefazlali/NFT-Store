from django.db import models

# Create your models here.


class Create(models.Model):
    title = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)
    email = models.EmailField()
    price = models.FloatField()
    benefit = models.CharField(max_length=255)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    Active = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توکن'
        verbose_name_plural = 'توکن ها'
        ordering = ['-created_time']


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/Category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Collection(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='collection/', null=True)
    hot = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
