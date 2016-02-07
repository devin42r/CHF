# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1453405137.295284
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        __M_writer('\n    <h1>Frequently Asked Questions</h1>\n    <div class="panel-group" id="accordion">\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapse1">\n            Collapsible Group 1</a>\n          </h4>\n        </div>\n        <div id="collapse1" class="panel-collapse collapse in">\n          <div class="panel-body">Lorem ipsum dolor sit amet, consectetur adipisicing elit,\n          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\n          minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea\n          commodo consequat.</div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapse2">\n            Collapsible Group 2</a>\n          </h4>\n        </div>\n        <div id="collapse2" class="panel-collapse collapse">\n          <div class="panel-body">Lorem ipsum dolor sit amet, consectetur adipisicing elit,\n          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\n          minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea\n          commodo consequat.</div>\n        </div>\n      </div>\n      <div class="panel panel-default">\n        <div class="panel-heading">\n          <h4 class="panel-title">\n            <a data-toggle="collapse" data-parent="#accordion" href="#collapse3">\n            Collapsible Group 3</a>\n          </h4>\n        </div>\n        <div id="collapse3" class="panel-collapse collapse">\n          <div class="panel-body">Lorem ipsum dolor sit amet, consectetur adipisicing elit,\n          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\n          minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea\n          commodo consequat.</div>\n        </div>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


