from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

