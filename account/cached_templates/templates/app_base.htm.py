# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1455554607.4630272
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['menu_image', 'navbar']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def menu_image():
            return render_menu_image(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        # SOURCE LINE 64
        __M_writer('\n\n    <div>request.path = ')
        # SOURCE LINE 66
        __M_writer(str( request.path ))
        __M_writer('</div>\n\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_image(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_image():
            return render_menu_image(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer('\n                        <img src="')
        # SOURCE LINE 18
        __M_writer(str( STATIC_URL ))
        __M_writer('/homepage/media/Images/CHF.png" alt="Colonial Heritage Foundation" height="50px">\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def navbar():
            return render_navbar(context)
        def menu_image():
            return render_menu_image(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n        <nav class="navbar-inverse navbar-default">\n          <div class="container-fluid">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n                <a class="" href="/homepage">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_image'):
            context['self'].menu_image(**pageargs)
        

        # SOURCE LINE 19
        __M_writer('\n                </a>\n              <!--<a class="navbar-brand" href="#">Brand</a>-->\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                <li class="')
        # SOURCE LINE 27
        __M_writer(str( 'active' if request.dmp_router_page == 'signup' else '' ))
        __M_writer('"><a href="/signup">Signup <span class="sr-only">(current)</span></a></li>\n                <li class="')
        # SOURCE LINE 28
        __M_writer(str( 'active' if request.dmp_router_page == 'login' else '' ))
        __M_writer('"><a href="/account/login">Login</a></li>\n                  <li class="')
        # SOURCE LINE 29
        __M_writer(str( 'active' if request.dmp_router_page == 'change' else '' ))
        __M_writer('"><a href="/account/change">Change Account Info</a></li>\n')
        # SOURCE LINE 60
        __M_writer('              </ul>\n            </div><!-- /.navbar-collapse -->\n          </div><!-- /.container-fluid -->\n        </nav>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


