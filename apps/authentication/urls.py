# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import OulougLoginView, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', OulougLoginView.as_view(), name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
