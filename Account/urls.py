from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('logged/', views.logged, name='logged'),
    path('signedup/', views.signedup, name='signedup'),
    path('login/', views.login_views, name='login'),
    path('signup/', views.signup_views, name='signup'),
    path('logout/', views.logout_views, name='logout')
]
