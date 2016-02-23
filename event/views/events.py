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
    events = emod.Event.objects.all().order_by('name')

    template_vars = {
        'events': events,
    }

    return dmp_render_to_response(request, 'events.html', template_vars)


@view_function
def edit(request):
    '''Edits an event'''
    try:
        events = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/event/events')
    form = EditForm(initial=model_to_dict(events))

    if request.method == 'POST': # just submitted the form
        form = EditForm(request.POST)
        form.event = events
        if form.is_valid():
            u = events
            u.name = form.cleaned_data.get('name')
            u.description = form.cleaned_data.get('description')
            u.start_date = form.cleaned_data.get('start_date')
            u.end_date = form.cleaned_data.get('end_date')
            u.venue = form.cleaned_data.get('venue')
            u.save()

            return HttpResponseRedirect('/event/events')

    Areas = emod.Area.objects.all().order_by('name').filter(event_id=events.id)
    template_vars = {
        'event': events,
        'form': form,
        'areas': Areas,
    }
    return dmp_render_to_response(request, 'events.edit.html', template_vars)

@view_function
class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # start_date = forms.CharField(label='Start Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # end_date = forms.CharField(label='End Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    start_date = forms.DateField(label='Start Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={"class":"form-control", "id":"datetimepicker"}))
    end_date = forms.DateField(label='End Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={"class":"form-control", "id":"datetimepicker2"}))
    venue = forms.ModelChoiceField(label='Venue', required=False, queryset=emod.Venue.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.event.name != self.cleaned_data.get('name'):
            try:
                product = emod.Event.objects.get(name=self.cleaned_data.get('name'))
                raise forms.ValidationError('This name has been taken.')
            except emod.Event.DoesNotExist:
                pass # this is what we hope happens - name is free
        return name


@view_function
def create(request):
    '''Creates an events'''
    form = CreateForm()
    if request.method == 'POST': # just submitted the form
        form = CreateForm(request.POST)
        if form.is_valid():
            # print('>>>>>>>>>>>>>>>>>> THE FORM IS VALID?')
            u = emod.Event()
            u.name = form.cleaned_data.get('name')
            u.description = form.cleaned_data.get('description')
            u.start_date = form.cleaned_data.get('start_date')
            u.end_date = form.cleaned_data.get('end_date')
            u.venue = form.cleaned_data.get('venue')
            u.save()
            return HttpResponseRedirect('/event/events')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'events.create.html', template_vars)


class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    start_date = forms.CharField(label='Start Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    end_date = forms.CharField(label='End Date', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    venue = forms.ModelChoiceField(label='Venue', queryset=emod.Venue.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            event = emod.Event.objects.get(name=self.cleaned_data.get('name'))
            raise forms.ValidationError('This name has been taken.')
        except emod.Event.DoesNotExist:
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
    '''Deletes an event'''
    try:
        event = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/event/events')

    event.delete()

    return HttpResponseRedirect('/event/events')
