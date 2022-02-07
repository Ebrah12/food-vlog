from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path('Login',views.login,name='Login'),
    path('Logout', views.logoutu, name='Logout'),
    path('Registration', views.register, name='Registration'),

]
