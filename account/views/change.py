from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from account.models import User

@view_function
def process_request(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login')

    # process the form (ie validation)
    form = ChangeForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'address': request.user.address1,
        'address2': request.user.address2,
    })
    if request.method == 'POST': # just submitted the form
        print('>>>>>>>>>>>HERE IN POST')
        form = ChangeForm(request.POST)
        if form.is_valid():
            u = request.user
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address')
            u.address2 = form.cleaned_data.get('address2')
            u.save()
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'change.html', template_vars)


class ChangeForm(forms.Form):
    '''The change form'''
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

        # def clean_username(self):
        #     username = self.cleaned_data.get('username')
        #     if not username.lower().strip().startswith('a'):
        #         raise forms.ValidationError('Please start your username with the letter"a".')
        #
        #     # check availability of username
        #     try:
        #         user = User.objects.get(username=self.cleaned_data.get('username'))
        #         raise forms.ValidationError('This username has been taken.')
        #     except User.DoesNotExist:
        #         pass # this is what we hope happens - username is free
        #
        #     # check the availability of the username (method #2)
        #     users = User.objects.filter(username=self.cleaned_data.get('username'))
        #     if len(users) > 0:
        #         raise forms.ValidationError('This username has been taken.')
        #     return username
        #
        #     # method number three
        #     if User.objects.filter(username=username).count() > 0:
        #         raise forms.ValidationError('This username has been taken')
        #     return username

        # def clean(self):
        #     if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
        #         raise forms.ValidationError('Your passwords need to match.  Please try again.')
        #     return self.cleaned_data
