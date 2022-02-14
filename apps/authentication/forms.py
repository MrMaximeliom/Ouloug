# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    second_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Second Name",
                "class": "form-control"
            }
        ))
    third_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Third Name",
                "class": "form-control"
            }
        ))
    fourth_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Fourth Name",
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Starts without country code)",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control",
                "disabled":"disabled"
            }


        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2','first_name',
                  'second_name','third_name','fourth_name','phone_number')
    def create(self, validated_data):
        from .models import User
        print("creating new user")
        user = User.objects.create(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                second_name=validated_data['second_name'],
                third_name=validated_data['third_name'],
                fourth_name=validated_data['fourth_name'],
                email=validated_data['email'],
                phone_number=validated_data['phone_number'],
            )
        user.set_password(validated_data['password'])

        user.save()
        return user

    def update(self, instance, validated_data):
        instance.phone_number = validated_data['phone_number']
        instance.first_name = validated_data['first_name']
        instance.second_name = validated_data['second_name']
        instance.third_name = validated_data['third_name']
        instance.fourth_name = validated_data['fourth_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])

        instance.save()
        return instance
