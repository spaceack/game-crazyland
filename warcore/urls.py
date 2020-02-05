from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path(r'register', views.register, name='register'),
    path(r'login', views.login, name='login'),
    path('regist', views.regist),
]