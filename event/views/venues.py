from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from event import models as emod
from account import models as mmod
from django.forms.models import model_to_dict
from django.contrib.admin.views.decorators import staff_member_required
# from homepage.customform import CustomForm
# from django.contrib.auth.models import User, Permission, Group


# @user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all())
# @staff_member_required

@view_function
def process_request(request):
    venues = emod.Venue.objects.all().order_by('name')

    template_vars = {
        'venues': venues,
    }

    return dmp_render_to_response(request, 'venues.html', template_vars)


@view_function
def edit(request):
    '''Edits a venue'''
    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/event/venues')
    form = EditForm(initial=model_to_dict(venue))

    if request.method == 'POST': # just submitted the form
        form = EditForm(request.POST)
        form.venues = venue
        if form.is_valid():
            u = venue
            u.name = form.cleaned_data.get('name')
            u.address = form.cleaned_data.get('address')
            u.city = form.cleaned_data.get('city')
            u.state = form.cleaned_data.get('state')
            u.zip_code = form.cleaned_data.get('zip_code')
            u.save()

            return HttpResponseRedirect('/event/venues')

    template_vars = {
        'venue': venue,
        'form': form,
    }
    return dmp_render_to_response(request, 'venues.edit.html', template_vars)


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.venues.name != self.cleaned_data.get('name'):
            try:
                venue = emod.Venue.objects.get(name=self.cleaned_data.get('name'))
                raise forms.ValidationError('This name has been taken.')
            except emod.Venue.DoesNotExist:
                pass # this is what we hope happens - name is free
        return name


@view_function
def create(request):
    '''Creates a venues'''
    form = CreateForm()
    if request.method == 'POST': # just submitted the form
        form = CreateForm(request.POST)
        if form.is_valid():
            # print('>>>>>>>>>>>>>>>>>> THE FORM IS VALID?')
            u = emod.Venue()
            u.name = form.cleaned_data.get('name')
            u.address = form.cleaned_data.get('address')
            u.city = form.cleaned_data.get('city')
            u.state = form.cleaned_data.get('state')
            u.zip_code = form.cleaned_data.get('zip_code')
            u.save()
            return HttpResponseRedirect('/event/venues')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'venues.create.html', template_vars)


class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            venue = emod.Venue.objects.get(name=self.cleaned_data.get('name'))
            raise forms.ValidationError('This name has been taken.')
        except emod.Venue.DoesNotExist:
            pass # this is what we hope happens - product name is free
        return name

    # def clean_phone_no(self):
    #     phone_no = self.cleaned_data.get('phone_number')
    #     try:
    #         int(phone_no)
    #     except (ValueError, TypeError):
    #         raise forms.ValidationError('Please enter a valid phone number')
    #     return phone_no

@view_function
def delete(request):
    '''Deletes a venue'''
    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/event/venues')

    venue.delete()

    return HttpResponseRedirect('/event/venues')