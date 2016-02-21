from django.db import models
from django.contrib import admin

# Define models here

class Venue(models.Model):
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip_code = models.TextField(null=True, blank=True)

admin.site.register(Venue)

#######################################################################################

class Event(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    venue = models.ForeignKey(Venue)

admin.site.register(Event)
#######################################################################################

class Area(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    place_number = models.TextField(null=True, blank=True)
    event = models.ForeignKey(Event)

admin.site.register(Area)