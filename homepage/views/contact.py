from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):
    print('>>>>>>>>>>>>>>>>>>>>> IN VIEW')

    clientemail = request.POST.get('email')
    clientmessage = request.POST.get('comment')
    print('>>>>>>>>>> email was', clientemail)
    print('>>>>>>>>>> message was', clientmessage)


    template_vars={
    }
    return dmp_render_to_response(request, 'signup.html', template_vars)