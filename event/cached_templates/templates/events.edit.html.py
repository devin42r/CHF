# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1456211229.3489614
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/event/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        event = context.get('event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 69
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        event = context.get('event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n    <h1 class="center">Edit ')
        # SOURCE LINE 7
        __M_writer(str( event.name ))
        __M_writer('</h1>\n    <h4 class="center"></h4>\n    <form method="POST" role="form">\n        <table id="myform">\n            ')
        # SOURCE LINE 11
        __M_writer(str( form.as_table() ))
        __M_writer('\n        </table>\n        <div class="row">\n            <div class="col-md-2">\n                <input type="submit" class="btn btn-warning" value="Save" />\n            </div>\n        </div>\n    </form>\n\n      <p class="text-right"><a href="/event/areas.create/')
        # SOURCE LINE 20
        __M_writer(str( event.id ))
        __M_writer('" class="btn btn-primary">Create Area</a></p>\n\n    <table class="table table-striped">\n        <tr>\n            <th>Name</th>\n            <th>Description</th>\n            <th>Place Number</th>\n            <th>Event</th>\n            <th>Action</th>\n        </tr>\n\n')
        # SOURCE LINE 31
        for area in areas:
            # SOURCE LINE 32
            __M_writer('            <tr>\n                <td>')
            # SOURCE LINE 33
            __M_writer(str( area.name ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 34
            __M_writer(str( area.description ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 35
            __M_writer(str( area.place_number ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 36
            __M_writer(str( area.event ))
            __M_writer('</td>\n                <td>\n                    <a href="/event/areas.edit/')
            # SOURCE LINE 38
            __M_writer(str( area.id ))
            __M_writer('/')
            __M_writer(str( event.id ))
            __M_writer('">Edit</a>\n                    |\n                    <a class="delete" href="/event/areas.delete/')
            # SOURCE LINE 40
            __M_writer(str( area.id ))
            __M_writer('/')
            __M_writer(str( event.id ))
            __M_writer('">Delete</a>\n                </td>\n            </tr>\n')
        # SOURCE LINE 44
        __M_writer('    </table>\n\n    <!-- Modal -->\n        <div id="delete_modal" class="modal fade" tabindex="-1" role="dialog">\n          <div class="modal-dialog" role="document">\n\n            <!-- Modal content-->\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title" id="MyModalLabel">Are You Sure?</h4>\n              </div>\n              <div class="modal-body">\n                <p>Delete the event</p>\n              </div>\n              <div class="modal-footer">\n                <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n                <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n              </div>\n            </div>\n\n          </div>\n        </div>\n\n\n')
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
        __M_writer('CHF Edit Event')
        return ''
    finally:
        context.caller_stack._pop_frame()


