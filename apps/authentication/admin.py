# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# from django import forms
from django.contrib import admin
from apps.authentication.models import User

admin.site.register(User)
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core.exceptions import ValidationError
#
#
#
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = "__all__"
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#
#     class Meta:
#         model = User
#         fields = "__all__"
#
#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'admin')
#     list_filter = ('admin','groups')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name','second_name','third_name','fourth_name','username','phone_number')}),
#         ('Permissions', {'fields': ('admin','user_type','staff','groups','is_superuser')}),
#         ('User Status', {'fields': ('user_status',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name',
#                        'second_name',
#                        'third_name',
#                        'fourth_name',
#                        'username',
#                        'user_type',
#                        'user_status',
#                        'phone_number',
#                        'staff',
#                        'admin',
#                        'password1',
#                        'password2'),
#         }),
#     )
#     search_fields = ('email','username')
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# # Now register the new UserAdmin...

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.