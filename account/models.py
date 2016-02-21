from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django import forms


# Define models here
class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debuggingpurposes'''
        return 'Users: %s (%s)' % (self.get_full_name(), self.username)

admin.site.register(User)


# class UserAttributes(forms.Form):
#     username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     # password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control" }))
#     # password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control" }))
#     address = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#     birth = forms.DateField(label='Birth', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms)
#     phone_number = forms.CharField(label='Phone Number', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')

    # other fields here

    # TEXT Field is usually slower except for postgres

    # python3 manage.py makemigrations account
    # python3 manage.py migrate