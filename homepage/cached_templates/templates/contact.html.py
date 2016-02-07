# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1453415112.8009856
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/homepage/templates/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n    <br>\n     <form role="form" method="POST">\n      <div class="form-group">\n        <label for="email">Email address:</label>\n        <input type="email" class="form-control" id="email" name="email">\n      </div>\n       <div class="form-group">\n          <label for="comment">Message:</label>\n          <textarea class="form-control" rows="5" id="comment" name="comment"></textarea>\n       </div>\n      <button type="submit" class="btn btn-default">Submit</button>\n    </form>\n    <br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


