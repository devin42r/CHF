# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1453404820.2546308
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\n     <h1>Education Exhibits</h1>\n        At its heart, the Foundation is an educational institution.  One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America\'s colonial period and is founding generation.  To this end, the Foundation has developed a variety of traveling exhibits.  One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.  The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence.\n    <h1>Apprenticeships</h1>\n        The Foundation seeks to help individuals who have developed skills peculiar to America\'s founding era to pass those skills on to others. One way to preserve these skills is to teach them to younger individuals. The Foundation seeks to match skilled artisans and craftsmen with eager young individuals for the purposing of learning trade and artistic skills.\n    <h1>Internships</h1>\n        Studies or History Education.  Individuals selected for the program spend one to three months accompanying educational exhibits to schools, teaching students about Colonial American History and portraying notable figures from the period.\n    <h1>Legal</h1>\n        The name "Colonial Heritage Foundation" is another name for the Society for the Preservation of America\'s Founding Values, Inc., which is a 501(3)(c) public charity.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


