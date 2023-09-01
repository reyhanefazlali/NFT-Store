from django.db import models
from django.contrib.auth.models import User
from web.models import Category, Collection


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    Artist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Bid_now = models.CharField(max_length=100)
    Bid_future = models.CharField(max_length=100)
    token_id = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='store/', null=True)
    Active = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    collection = models.ManyToManyField(Collection)
    image_details = models.ImageField(upload_to='store/details/', null=True)

    def __str__(self):
        return self.title


class Author(models.Model):

    Adult = 'adult'
    TeenAger = 'teenager'
    Child = 'child'

    Age_fields = (
        (Adult, 'adult'),
        (TeenAger, 'teenager'),
        (Child, 'child'))

    name = models.CharField(max_length=255)
    Family = models.CharField(max_length=255)
    Age = models.IntegerField()
    National_ID = models.IntegerField()
    Followers = models.IntegerField()
    income = models.FloatField()
    username = models.ManyToManyField(User)
    posts = models.ManyToManyField(Post)
    age_category = models.CharField(
        max_length=255, choices=Age_fields, default=Adult)

    def __str__(self):
        self.fullname = self.name + " " + self.Family
        return self.fullname


class BidDetail(models.Model):
    customer_bid = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.customer_bid
