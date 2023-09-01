from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('<int:num>', views.details, name='details'),
    path('author/<str:auth>', views.author, name='author'),
]
