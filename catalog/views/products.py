from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from catalog import models as amod
from catalog import models as mmod
from account import models as accmod
from django.forms.models import model_to_dict
from django.contrib.admin.views.decorators import staff_member_required
# from homepage.customform import CustomForm
import random

# @user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all())
# @staff_member_required

@view_function
def process_request(request):
    # bulkproducts = amod.BulkProduct.objects.all().order_by('name')
    # individualproducts = amod.IndividualProduct.objects.all().order_by('name')
    # rentalproducts = amod.RentalProduct.objects.all().order_by('name')
    products = amod.Product.objects.all()

    template_vars = {
        'products': products,
        # 'bulkproducts': bulkproducts,
        # 'individualproducts': individualproducts,
        # 'rentalproducts': rentalproducts,
    }

    return dmp_render_to_response(request, 'products.html', template_vars)


@view_function
def edit(request):
    '''Edits a product'''
    try:
        product = amod.Product.objects.get(id=request.urlparams[0])
    except amod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/products/')
    form = EditForm(initial=model_to_dict(product))

    if request.method == 'POST': # just submitted the form
        form = EditForm(request.POST)
        form.products = product
        if form.is_valid():
            p = product

            # specialized attributes ##########################

            if form.cleaned_data.get('quantity') != '':
                print('HERE IN QUANTITY')
                p.quantity = form.cleaned_data.get('quantity')

            if form.cleaned_data.get('purchase_date') != '':
                p.purchase_date = form.cleaned_data.get('creator')

            p.creator = form.cleaned_data.get('creator')
            p.status = form.cleaned_data.get('status')

            # if form.cleaned_data.get('status') == 'current':
            #     p.status = 'Rentable'
            # elif form.cleaned_data.get('status') == 'damaged':
            #     p.status = 'Damaged'
            # elif form.cleaned_data.get('status') == 'retired':
            #     p.status = 'No Longer Rentable'
            # elif form.cleaned_data.get('status') == 'dirty':
            #     p.status = 'Dirty'

            p.name = form.cleaned_data.get('name')
            p.description = form.cleaned_data.get('description')
            p.image = form.cleaned_data.get('image')
            p.save()
            return HttpResponseRedirect('/catalog/products')

    template_vars = {
        'product': product,
        'form': form,
    }
    return dmp_render_to_response(request, 'products.edit.html', template_vars)

    # show edit form html


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={"class":"form-control"}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    quantity = forms.CharField(label='Quantity', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"quantity"}))
    creator = forms.CharField(label='Creator', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"creator"}))
    purchase_date = forms.CharField(label='Purchase Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"purchase"}))
    status = forms.ChoiceField(choices=mmod.RENTAL_STATUS_CHOICES, label='Status', required=False, widget=forms.Select(attrs={"class":"form-control hideThis", "id":"status"}))
    # days = forms.ModelChoiceField(queryset=Books.objects.all().order_by('name'))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.products.name != self.cleaned_data.get('name'):
            try:
                product = mmod.Product.objects.get(name=self.cleaned_data.get('name'))
                raise forms.ValidationError('This name has been taken.')
            except mmod.Product.DoesNotExist:
                pass # this is what we hope happens - name is free
        return name


@view_function
def create(request):
    '''Creates a product'''
    form = CreateForm()
    if request.method == 'POST': # just submitted the form
        print('submitted form')
        form = CreateForm(request.POST)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>> THE FORM IS VALID?')
            if form.cleaned_data.get('product_type') == 'BP':
                print('>>>>>>>>>>>>>>>>>> IN THE BP?')
                p = mmod.BulkProduct()
                p.quantity = form.cleaned_data.get('quantity')
            elif form.cleaned_data.get('product_type') == 'IP':
                p = mmod.IndividualProduct()
                p.creator = form.cleaned_data.get('creator')
            else:
                p = mmod.RentalProduct()
                p.purchase_date = form.cleaned_data.get('purchase')
                p.status = form.cleaned_data.get('status')

                # if form.cleaned_data.get('status') == 'current':
                #     p.status = 'Rentable'
                # elif form.cleaned_data.get('status') == 'damaged':
                #     p.status = 'Damaged'
                # elif form.cleaned_data.get('status') == 'retired':
                #     print('>>>>>> HERE ')
                #     p.status = 'No Longer Rentable'
                # else:
                #     p.status = 'Dirty'

                # mydict = dict(PRODUCT_TYPE_CHOICES)
                # mydict[""]
                # george = form.cleaned_data['status']
                # hey = mmod.RENTAL_STATUS_CHOICES(george)
                #
                # print('>>>>>>>' + hey)
                #
                # # Let's get the dictionary value of status
                # def get_item(dictionary, key):
                #     return dictionary.get(key)
                # george = form.cleaned_data['status']
                # # mmod.RENTAL_STATUS_CHOICES|get_item:george
                #
                #
                # # george = mmod.RENTAL_STATUS_CHOICES_MAP(george)
                # # print('>>>>>>>' + george)

            p.name = form.cleaned_data.get('name')
            p.description = form.cleaned_data.get('description')
            p.image = form.cleaned_data.get('image')
            p.category = mmod.Category.objects.get(id=1)
            p.save()
            return HttpResponseRedirect('/catalog/products')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'products.create.html', template_vars)

PRODUCT_TYPE_CHOICES = (
    ('BP', 'Bulk Product'),
    ('IP', 'Individual Product'),
    ('RP', 'Rental Product'),
)


class CreateForm(forms.Form):
    product_type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES, label='Product Type', required=True, widget=forms.Select(attrs={"class":"form-control"}))
    creator = forms.ModelChoiceField( label='Creator', required=False, queryset=accmod.User.objects.all().order_by('last_name'), widget=forms.Select(attrs={"class":"form-control hideThis", "id":"creator"}))
    purchase_date = forms.CharField(label='Purchase Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"purchase"}))
    status = forms.ChoiceField(choices=mmod.RENTAL_STATUS_CHOICES, label='Status', required=False, widget=forms.Select(attrs={"class":"form-control hideThis", "id":"status"}))
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    quantity = forms.CharField(label='Quantity', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"quantity"}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={"class":"form-control"}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    # creator = forms.CharField(label='Creator', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control hideThis", "id":"creator"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            product = mmod.Product.objects.get(name=self.cleaned_data.get('name'))
            raise forms.ValidationError('This name has been taken.')
        except mmod.Product.DoesNotExist:
            pass # this is what we hope happens - product name is free
        return name


@view_function
def delete(request):
    '''Deletes a product'''
    print('were here')
    try:
        product = amod.Product.objects.get(id=request.urlparams[0])
    except amod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/products')

    product.delete()

    return HttpResponseRedirect('/catalog/products')