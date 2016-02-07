# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1454785707.4638553
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/account/templates/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        error_message = context.get('error_message', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n')
        # SOURCE LINE 5
        __M_writer(str( error_message ))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\n    <br>\n\n     <form action="/account/signup/" role="form" method="POST">\n         <table>\n            ')
        # SOURCE LINE 12
        __M_writer(str( form ))
        __M_writer('\n         </table>\n      <!--\n      <div class="form-group">\n        <label for="First_Name">First Name</label>\n        <input type="text" class="form-control" id="First_Name" name="firstname">\n      </div>\n      <div class="form-group">\n        <label for="Last_Name">Last Name</label>\n        <input type="text" class="form-control" id="Last_Name" name="lastname">\n      </div>\n      <div class="form-group">\n        <label for="Email">Email address</label>\n        <input type="email" class="form-control" id="Email" name="email">\n      </div>\n      <div class="form-group">\n          <label for="Password">Password</label>\n          <input class="form-control" id="Password" name="password">\n      </div>\n      <div class="form-group">\n          <label for="Password2">Confirm Password</label>\n          <input class="form-control" id="Password2" name="password2">\n      </div> -->\n      <input type="submit" class="btn btn-default">Submit</input>\n    </form>\n    <br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('Sign Up')
        return ''
    finally:
        context.caller_stack._pop_frame()


