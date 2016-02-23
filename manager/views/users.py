from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from account import models as amod
from account import models as mmod
from django.forms.models import model_to_dict
from django.contrib.admin.views.decorators import staff_member_required
# from homepage.customform import CustomForm
from django.contrib.auth.models import User, Permission, Group


# @user_passes_test(lambda u: Group.objects.get(name='Baristas') in u.groups.all())
# @staff_member_required

@view_function
def process_request(request):
    users = amod.User.objects.all().order_by('last_name', 'first_name')

    template_vars = {
        'users': users,
    }

    return dmp_render_to_response(request, 'users.html', template_vars)


@view_function
def edit(request):
    '''Edits a user'''
    try:
        users = amod.User.objects.get(id=request.urlparams[0])
        print('\nUSER: ' + users.first_name)
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')
    form = EditForm(initial=model_to_dict(users))

    if request.method == 'POST': # just submitted the form
        form = EditForm(request.POST)
        form.user = users
        if form.is_valid():
            u = users
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address')
            u.address2 = form.cleaned_data.get('address2')
            u.city = form.cleaned_data.get('city')
            u.birth = form.cleaned_data.get('birth')
            u.save()
            u.groups.clear()

            for group in form.cleaned_data['groups']:
                print(group)
                u.groups.add(group)
            u.save()

            u.user_permissions.clear()

            for permission in form.cleaned_data['user_permissions']:
                u.user_permissions.add(permission)

            u.save()

            return HttpResponseRedirect('/manager/users/')

    template_vars = {
        'users': users,
        'form': form,
    }
    return dmp_render_to_response(request, 'users.edit.html', template_vars)

    # show edit form html


class EditForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    # password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address1 = forms.CharField(label='Address 1', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    birth = forms.DateField(label='Birth', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={"class":"form-control", "id":"datetimepicker"}))
    phone_number = forms.CharField(label='Phone Number', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    groups = forms.ModelMultipleChoiceField(label='Group', required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    user_permissions = forms.ModelMultipleChoiceField(label='Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.user.username != self.cleaned_data.get('username'):
            try:
                user = mmod.User.objects.get(username=self.cleaned_data.get('username'))
                raise forms.ValidationError('This username has been taken.')
            except mmod.User.DoesNotExist:
                pass # this is what we hope happens - username is free
        return username


@view_function
def create(request):
    '''Creates a users'''
    form = CreateForm()
    if request.method == 'POST': # just submitted the form
        form = CreateForm(request.POST)
        if form.is_valid():
            # print('>>>>>>>>>>>>>>>>>> THE FORM IS VALID?')
            u = mmod.User()
            u.username = form.cleaned_data.get('username')
            u.set_password(form.cleaned_data.get('password'))
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.city = form.cleaned_data.get('city')
            u.birth(form.cleaned_data.get('birth'))
            u.address1 = form.cleaned_data.get('address')
            u.address2 = form.cleaned_data.get('address2')
            u.save()
            return HttpResponseRedirect('/manager/users')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.create.html', template_vars)


class CreateForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    birth = forms.DateField(label='Birth', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={"class":"form-control", "id":"datetimepicker"}))
    phone_number = forms.CharField(label='Phone Number', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = mmod.User.objects.get(username=self.cleaned_data.get('username'))
            raise forms.ValidationError('This username has been taken.')
        except mmod.User.DoesNotExist:
            pass # this is what we hope happens - username is free
        return username

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_number')
        try:
            int(phone_no)
        except (ValueError, TypeError):
            raise forms.ValidationError('Please enter a valid phone number')
        return phone_no

@view_function
def delete(request):
    '''Deletes a user'''
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    user.delete()

    return HttpResponseRedirect('/manager/users/')


@view_function
def password_change(request):
    '''Let's change the password'''
    # if not request.user.is_authenticated():
    #     return HttpResponseRedirect('/manager/users')
    try:
        print(">>>>>>>>>>>>>>HERE:" + request.urlparams[0])
        users = amod.User.objects.get(id=request.urlparams[0])
        # print('\nUSER: ' + users.first_name)
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('manager/users/')

    # process the form (ie validation)
    form = pChangeForm()
    if request.method == 'POST': # just submitted the form
        form = pChangeForm(request.POST)
        form.user = request.user
        if form.is_valid():
            u = users
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return HttpResponseRedirect('/manager/users')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'user.password.change.html', template_vars)


class pChangeForm(forms.Form):
    '''The pchange form'''
    password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control"}))
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control" }))

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match.  Please try again.')
        return self.cleaned_data