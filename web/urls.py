from django.urls import path
from . import views


app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('<str:col>', views.explore, name='collection'),
    path('create/', views.create, name='create'),
    path('category/<str:cat>', views.items, name='category'),
    path('search/', views.search_post, name='search'),
]
