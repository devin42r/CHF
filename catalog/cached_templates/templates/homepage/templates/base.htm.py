# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1455769401.1813033
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_left', 'footer', 'navbar', 'title', 'content', 'username', 'header', 'main_body', 'maintenance', 'top', 'alert', 'content_right']


# SOURCE LINE 4
from django_mako_plus.controller import static_files 

# SOURCE LINE 5
import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def username():
            return render_username(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def main_body():
            return render_main_body(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def maintenance():
            return render_maintenance(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n    <link href="')
        # SOURCE LINE 13
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Images/favicon.ico" rel="shortcut icon" type="image/x-icon" />\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 14
        __M_writer('</title>\n    \n')
        # SOURCE LINE 17
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n      <script src="')
        # SOURCE LINE 18
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n      <script src="')
        # SOURCE LINE 19
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.min.js"></script>\n      <script src="')
        # SOURCE LINE 20
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/moment.js"></script>\n      <script src="')
        # SOURCE LINE 21
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.js"></script>\n\n\n    <link rel="stylesheet" href="')
        # SOURCE LINE 24
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Bootstrap3/css/bootstrap.min.css" />\n      <link rel="stylesheet" href="')
        # SOURCE LINE 25
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.css" />\n  \n')
        # SOURCE LINE 28
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n\n  <body>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_body'):
            context['self'].main_body(**pageargs)
        

        # SOURCE LINE 84
        __M_writer('\n\n    <footer id="footer" style="text-align:center">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 89
        __M_writer('\n    </footer>\n\n    <script src="')
        # SOURCE LINE 92
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Bootstrap3/js/bootstrap.min.js"></script>\n\n')
        # SOURCE LINE 95
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer('\n\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer('\n        <p class="footer-text">Copyright &copy; Devin Rasmussen ')
        # SOURCE LINE 88
        __M_writer(str( datetime.date.today().year ))
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def username():
            return render_username(context)
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer('\n\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'username'):
            context['self'].username(**pageargs)
        

        # SOURCE LINE 45
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer('Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 72
        __M_writer('\n                            CENTER AREA\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_username(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def username():
            return render_username(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance():
            return render_maintenance(context)
        def header():
            return render_header(context)
        def username():
            return render_username(context)
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer('\n\n          <div id="maintenance_message">\n\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance'):
            context['self'].maintenance(**pageargs)
        

        # SOURCE LINE 40
        __M_writer('\n          </div>\n\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        # SOURCE LINE 47
        __M_writer('\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        def navbar():
            return render_navbar(context)
        def top():
            return render_top(context)
        def username():
            return render_username(context)
        def header():
            return render_header(context)
        def content():
            return render_content(context)
        def main_body():
            return render_main_body(context)
        def maintenance():
            return render_maintenance(context)
        def alert():
            return render_alert(context)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer('\n\n      <header>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 48
        __M_writer('\n      </header>\n\n          <div id="alert" class="alert alert-info">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        # SOURCE LINE 55
        __M_writer('\n          </div>\n\n\n            <div class="container clearfix">\n                <div class="row">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 63
        __M_writer('\n                </div>\n                <div class="row">\n                    <div class="col-md-2">\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        # SOURCE LINE 69
        __M_writer('\n                    </div>\n                    <div class="col-md-8">\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 74
        __M_writer('\n                    </div>\n                    <div class="col-md-2">\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        # SOURCE LINE 79
        __M_writer('\n                    </div>\n                </div>\n            </div>\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance():
            return render_maintenance(context)
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer('Site will go down tomorrow!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        # SOURCE LINE 61
        __M_writer('\n\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer('\n                <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>\n                <strong>Info!</strong> This alert box could indicate a neutral informative change or action.\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer('\n\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


