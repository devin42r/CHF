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
    areas = emod.Area.objects.all().order_by('name')

    template_vars = {
        'areas': areas,
    }

    return dmp_render_to_response(request, 'areas.html', template_vars)


@view_function
def edit(request):
    '''Edits a area'''
    try:
        areas = emod.Area.objects.get(id=request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect('/event/areas')
    form = EditForm(initial=model_to_dict(areas))

    if request.method == 'POST': # just submitted the form
        form = EditForm(request.POST)
        form.areas = areas
        if form.is_valid():
            u = areas
            u.name = form.cleaned_data.get('name')
            u.description = form.cleaned_data.get('description')
            u.place_number = form.cleaned_data.get('place_number')
            u.save()

            return HttpResponseRedirect('/event/events.edit/' + request.urlparams[1])

    template_vars = {
        'area': areas,
        'form': form,
    }
    return dmp_render_to_response(request, 'areas.edit.html', template_vars)


class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    place_number = forms.CharField(label='Place Number', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.areas.name != self.cleaned_data.get('name'):
            try:
                area = emod.Area.objects.get(name=self.cleaned_data.get('name'))
                raise forms.ValidationError('This name has been taken.')
            except emod.Area.DoesNotExist:
                pass # this is what we hope happens - name is free
        return name


@view_function
def create(request):
    '''Creates a areas'''
    form = CreateForm()
    if request.method == 'POST': # just submitted the form
        form = CreateForm(request.POST)
        if form.is_valid():
            u = emod.Area()
            u.name = form.cleaned_data.get('name')
            u.description = form.cleaned_data.get('description')
            u.place_number = form.cleaned_data.get('place_number')
            u.event = emod.Event.objects.get(id=request.urlparams[0])
            u.save()
            return HttpResponseRedirect('/event/events.edit/' + request.urlparams[0])

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'areas.create.html', template_vars)


class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    place_number = forms.CharField(label='Place Number', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            area = emod.Area.objects.get(name=self.cleaned_data.get('name'))
            raise forms.ValidationError('This name has been taken.')
        except emod.Area.DoesNotExist:
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
    '''Deletes a area'''
    try:
        area = emod.Area.objects.get(id=request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect('/event/areas')

    area.delete()

    return HttpResponseRedirect('/event/events.edit/' + request.urlparams[1])