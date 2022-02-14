# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from Util.static_strings import (
FIRST_NAME_EMPTY_ERROR,
FIRST_NAME_SYNTAX_ERROR,
SECOND_NAME_SYNTAX_ERROR,
SECOND_NAME_EMPTY_ERROR,
THIRD_NAME_EMPTY_ERROR,
THIRD_NAME_SYNTAX_ERROR,
FOURTH_NAME_EMPTY_ERROR,
FOURTH_NAME_SYNTAX_ERROR,
USERNAME_EMPTY_ERROR,
USERNAME_BAD_FORMAT,
PHONE_PHONE_EMPTY_ERROR,
PHONE_NUMBER_SYNTAX_ERROR,
EMAIL_EMPTY_ERROR,
EMAIL_SYNTAX_ERROR,
PASSWORD_EMPTY_ERROR,
PASSWORDS_NOT_MATCH,
CONFIRM_PASSWORD_EMPTY_ERROR
)

def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password")
            username = request.POST['username']
            password = request.POST['password']
            print("username is: ",username," password is: ",password)
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('first password',user.password)
            user.set_password(user.password)
            print("\nafter hashing:",user.password)
            user.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()


    return render(request, "accounts/register.html", {"form": form, "msg": msg,
                                                      "success": success,
                                                      'data_js': {
                                                          "first_name_empty_error": FIRST_NAME_EMPTY_ERROR,
                                                          "second_name_empty_error": SECOND_NAME_EMPTY_ERROR,
                                                          "third_name_empty_error": THIRD_NAME_EMPTY_ERROR,
                                                          "fourth_name_empty_error": FOURTH_NAME_EMPTY_ERROR,
                                                          "first_name_error": FIRST_NAME_SYNTAX_ERROR,
                                                          "second_name_error": SECOND_NAME_SYNTAX_ERROR,
                                                          "third_name_error": THIRD_NAME_SYNTAX_ERROR,
                                                          "fourth_name_error": FOURTH_NAME_SYNTAX_ERROR,
                                                          "email_empty_error": EMAIL_EMPTY_ERROR,
                                                          "email_error": EMAIL_SYNTAX_ERROR,
                                                          "username_empty_error":USERNAME_EMPTY_ERROR,
                                                          "username_error":USERNAME_BAD_FORMAT,
                                                          "phone_number_empty_error": PHONE_PHONE_EMPTY_ERROR,
                                                          "phone_number_error": PHONE_NUMBER_SYNTAX_ERROR,
                                                          "passwords_not_match":PASSWORDS_NOT_MATCH,
                                                          "password_empty_error":PASSWORD_EMPTY_ERROR,
                                                          "confirm_password_empty_error":CONFIRM_PASSWORD_EMPTY_ERROR

                                                      }
                                                      })
