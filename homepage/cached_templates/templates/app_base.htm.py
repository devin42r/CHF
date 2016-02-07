# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1454789762.6556094
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['navbar', 'menu_image']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def menu_image():
            return render_menu_image(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n<head>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        # SOURCE LINE 76
        __M_writer('\n\n    <div>request.path = ')
        # SOURCE LINE 78
        __M_writer(str( request.path ))
        __M_writer('</div>\n\n</head>\n<body>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar():
            return render_navbar(context)
        def menu_image():
            return render_menu_image(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\n        <nav class="navbar-inverse navbar-default">\n          <div class="container-fluid">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n                <a class="" href="/homepage">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_image'):
            context['self'].menu_image(**pageargs)
        

        # SOURCE LINE 21
        __M_writer('\n                </a>\n              <!--<a class="navbar-brand" href="#">Brand</a>-->\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                <li class="')
        # SOURCE LINE 29
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else '' ))
        __M_writer('"><a href="/about">About <span class="sr-only">(current)</span></a></li>\n                <li class="')
        # SOURCE LINE 30
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\n                <li class="dropdown">\n                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>\n                  <ul class="dropdown-menu">\n                    <li><a href="#">Action</a></li>\n                    <li><a href="#">Another action</a></li>\n                    <li><a href="#">Something else here</a></li>\n                    <li role="separator" class="divider"></li>\n                    <li><a href="#">Separated link</a></li>\n                    <li role="separator" class="divider"></li>\n                    <li><a href="#">One more separated link</a></li>\n                  </ul>\n                </li>\n              </ul>\n              <form class="navbar-form navbar-left" role="search">\n                <div class="form-group">\n                  <input type="text" class="form-control" placeholder="Search">\n                </div>\n                <button type="submit" class="btn btn-default">Submit</button>\n              </form>\n              <ul class="nav navbar-nav navbar-right">\n                <li><a href="#">Link</a></li>\n\n')
        # SOURCE LINE 53
        if request.user.is_authenticated():
            # SOURCE LINE 54
            __M_writer('                      <li class="dropdown">\n                          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Hello ')
            # SOURCE LINE 55
            __M_writer(str( request.user ))
            __M_writer(' <span class="caret"></span></a>\n                          <ul class="dropdown-menu">\n                            <li><a href="/account/change/">My Account</a></li>\n                            <li role="separator" class="divider"></li>\n                            <li><a href="/account/logout">Logout</a></li>\n                          </ul>\n                      </li>\n                      <!--<a href="/account/logout/" class="btn btn-warning">Logout</a>-->\n')
            # SOURCE LINE 63
        else:
            # SOURCE LINE 64
            __M_writer('                    <!-- Login -->\n')
            # SOURCE LINE 66
            __M_writer('                      <button id="loginbutton" type="button" class="btn btn-primary btn-lg">\n                        Login\n                      </button>\n')
        # SOURCE LINE 70
        __M_writer('\n\n              </ul>\n            </div><!-- /.navbar-collapse -->\n          </div><!-- /.container-fluid -->\n        </nav>\n    ')
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
        # SOURCE LINE 19
        __M_writer('\n                        <img src="')
        # SOURCE LINE 20
        __M_writer(str( STATIC_URL ))
        __M_writer('/homepage/media/Images/CHF.png" alt="Colonial Heritage Foundation" height="50px">\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


