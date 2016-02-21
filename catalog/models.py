from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel


class Category(models.Model):
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)

admin.site.register(Category)

#######################################################################################

class Product(PolymorphicModel):
    '''superclass of all products'''
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Product (abstract): %s (%s)' % (self.name, self.add_date)

admin.site.register(Product)


######################################################################################

RENTAL_STATUS_CHOICES = (
    ( 'current', 'Rentable'),
    ( 'damaged', 'Damaged'),
    ( 'retired', 'No Longer Rentable'),
    ( 'dirty', 'Dirty'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

class RentalProduct(Product):
    '''A product that is rentable'''
    purchase_date = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)
#   rental = models.ForeignKey('Rental' null=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Rental Products: %s (%s) %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)


######################################################################################

class IndividualProduct(Product):
    '''A product we track individually'''
    creator = models.ForeignKey('account.User')
    create_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Rental Products: %s (%s) %s' % (self.name, self.add_date, self.creator.get_full_name())

admin.site.register(IndividualProduct)


######################################################################################

class BulkProduct(Product):
    '''A product tracked by quantiy'''
    quantity = models.IntegerField(default=0)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Bulk Product: %s (%s) %s' % (self.name, self.add_date, self.quantity)

admin.site.register(BulkProduct)

#######################################################################################
