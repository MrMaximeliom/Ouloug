
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
import uuid

## CHANGELOG
# changes in 12-1-2022
# adding id field of type UUID as primary key for all models


"""
User Account Manager:
used as a user manager for the User model
"""


class UserAccountManager(BaseUserManager):
    # this function is responsible for creating users
    # the parameters passed to it are required to create user object
    def create_user(self, email, username, first_name, phone_number,password=None, **extra_fields):
        # check if username not null
        if not username:
            raise ValueError(_('Users must have a username'))
        # check if full_name not null
        if not first_name:
            raise ValueError(_('Users must provide their full name'))
        if not phone_number:
            raise ValueError(_('Users must provide their phone number'))
        if not email:
            raise ValueError(_('Users must provide their email'))

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            phone_number=phone_number,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, first_name, phone_number,
                         password):
        user = self.create_user(
            email=self.normalize_email(email),
        username=username,
            first_name=first_name,
            phone_number=phone_number,
            password=password,
        )
        # user.set_password(password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


"""
User Model:
it's used to save user's data
"""
USER_TYPES = (
    ("customer", "Customer"),
    ("customer_administrator", "Administrator Customer"),
    ("agent", "Agent"),
    ("team_leader", "Team Leader"),
    ("administrator", "Administrator"),
    ("special_administrator", "Special Administrator"),
    ("monitor", "Monitor"),
)
USER_STATUS = (
    ("active", "Active"),
    ("not_active", "Not Active"),
    ("suspended", "Suspended"),
    ("blocked", "Blocked"),
    ("deleted", "Deleted"),
)


class User(AbstractBaseUser):
    # this field represents the primary key of the model
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    # this field represents the first name
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=150,
        blank=False,
        null=False
    )
    # this field represents the second name
    second_name = models.CharField(
        verbose_name=_('Second Name'),
        max_length=150,
        blank=False,
        null=False
    )
    # this field represents the third name
    third_name = models.CharField(
        verbose_name=_('Third Name'),
        max_length=150,
        blank=False,
        null=False
    )
    # this field represents the fourth name
    fourth_name = models.CharField(
        verbose_name=_('Fourth Name'),
        max_length=150,
        blank=False,
        null=False
    )
    # this field represents the username
    username = models.CharField(
        verbose_name=_('User Name'),
        blank=False,
        null=False,
        max_length=150,
    )
    # this field represents the user type
    user_type = models.CharField(
        verbose_name=_('User Type'),
        max_length=100,
        blank=False,
        null=False,
        choices=USER_TYPES
    )
    # this field represents the user status
    user_status = models.CharField(
        verbose_name=_('User Status'),
        max_length=100,
        blank=False,
        null=False,
        choices=USER_STATUS)
    # this field represents the user phone number
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        blank=False,
        null=False,
        max_length=100,
        unique=True
    )
    # this field represents the email
    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    # this is a boolean field used to mark user as staff or not
    staff = models.BooleanField(default=False)
    # this is a boolean field used to mark user as admin or not
    admin = models.BooleanField(default=False)
    # this field represents the last login date and time
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    # this field represents the registration date and time
    registration_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # this field represents the username field
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'full_name',
                       'username']  # Email & Password are required by default.
    objects = UserAccountManager()

    def get_full_name(self):
        # The user is identified by their four names
        return str(self.first_name) + " " + str(self.second_name) + " " + str(self.third_name) + " " + str(
            self.fourth_name)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # return self.user_role == 3
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        # return self.user_role == 1
        return self.admin

    class Meta:
        # this is the actual model's name in the database
        db_table = "user"


# list of available statuses for a country
COUNTRY_STATUS = (
    ("Active", "Active"),
    ("Not Active", "Not Active"),
    ("Suspended", "Suspended"),
    ("On Hold", "On Hold")
)


