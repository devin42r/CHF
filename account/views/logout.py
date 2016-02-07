from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


@view_function
def process_request(request):
    # log the user out
    logout(request)

    # now what?

    return HttpResponseRedirect('/homepage/')
