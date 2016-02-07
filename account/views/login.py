from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from account.models import User

@view_function
def process_request(request):
    print('>>>>>>>>>>>>>>>>>>>>> IN login.py')

    # clientemail = request.POST.get('email')
    # clientmessage = request.POST.get('comment')
    # print('>>>>>>>>>> login,py email was', clientemail)
    # print('>>>>>>>>>> login.py message was', clientmessage)

    # process the form
    form = LoginForm()
    if request.method == 'POST': # just submitted the form
        form = LoginForm(request.POST)
        if form.is_valid():
            # log the user in
            # user = authenticate(username=form.cleaned_data.get('username')), password=form.cleaned_data.get('password'))
            login(request, form.user)
            print('>>>>>>>>>>>>>>>>JUST PAST LOGIN')
            # logout(request)
            # return HttpResponseRedirect('/homepage/index/') MODAL AJAX ISSUE
            return HttpResponse('''
            <script>
                window.location = '/homepage/index/';
            </script>
                ''')
            # window.location.reload()
            # window.location.href = '/homepage/index/'

    template_vars={
        'form':form,
    }
    return dmp_render_to_response(request, 'login.html', template_vars)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100)
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('The username and password was not found in our system')
        self.user = user
        return self.cleaned_data