from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from account.models import User



@view_function
def process_request(request):
    print('>>>>>>>>>>>>>>>>>>>>> THIS IS SIGNUP.PY')

    clientemail = request.POST.get('first_name')
    clientmessage = request.POST.get('last_name')
    print('>>>>>>>>>> fname was', clientemail)
    print('>>>>>>>>>> lname was', clientmessage)

    # process the form (ie validation)
    form = SignupForm()
    if request.method == 'POST': # just submitted the form
        form = SignupForm(request.POST)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>> THE FORM IS VALID?')
            u = User()
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.set_password(form.cleaned_data.get('password'))
            u.address1 = form.cleaned_data.get('address')
            u.address2 = form.cleaned_data.get('address2')
            u.save()
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'signup.html', template_vars)


class SignupForm(forms.Form):
    '''The signup form'''
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control" }))
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ "class": "form-control" }))
    address = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    address2 = forms.CharField(label='Address 2', required=False, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # if not username.lower().strip().startswith('a'):
        #     raise forms.ValidationError('Please start your username with the letter"a".')

        # check availability of username
        try:
            user = User.objects.get(username=self.cleaned_data.get('username'))
            raise forms.ValidationError('This username has been taken.')
        except User.DoesNotExist:
            pass # this is what we hope happens - username is free

        # check the availability of the username (method #2)
        users = User.objects.filter(username=self.cleaned_data.get('username'))
        if len(users) > 0:
            raise forms.ValidationError('This username has been taken.')
        return username

        # method number three
        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('This username has been taken')
        return username

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match.  Please try again.')
        return self.cleaned_data
