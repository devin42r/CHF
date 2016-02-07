from django.db import models
from django.contrib.auth.models import AbstractUser


# Define models here
class User(AbstractUser):
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    # other fields here

    # TEXT Field is usually slower except for postgres

    # python3 manage.py makemigrations account
    # python3 manage.py migrate