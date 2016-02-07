from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login')

    # process the form (ie validation)
    form = pChangeForm()
    if request.method == 'POST': # just submitted the form
        form = pChangeForm(request.POST)
        form.user = request.user
        if form.is_valid():
            u = request.user
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return HttpResponseRedirect('/homepage/index/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'pchange.html', template_vars)


class pChangeForm(forms.Form):
    '''The pchange form'''
    currentPassword = forms.CharField(label='Current Password', required=True, max_length=100, widget=forms.PasswordInput)
    password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput)

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

    def clean_currentPassword(self):
        if not self.user.check_password(self.cleaned_data.get('currentPassword')):
            raise forms.ValidationError('The current password does not seem to be correct')
        return self.cleaned_data.get('currentPassword')

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match.  Please try again.')
        return self.cleaned_data
