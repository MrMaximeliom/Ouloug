from django.urls import path
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

  ]
