# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1456172961.014399
_enable_loop = True
_template_filename = '/home/devin/PycharmProjects/CHF/event/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 56
        __M_writer('\n\n')
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
        __M_writer('CHF Current Venues')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n\n    <p class="text-right"><a href="/event/venues.create/" class="btn btn-primary">Create Venue</a></p>\n\n    <table class="table table-striped">\n        <tr>\n            <th>Name</th>\n            <th>Address</th>\n            <th>City</th>\n            <th>State</th>\n            <th>Zip Code</th>\n            <th>Action</th>\n        </tr>\n\n')
        # SOURCE LINE 19
        for venue in venues:
            # SOURCE LINE 20
            __M_writer('            <tr>\n                <td>')
            # SOURCE LINE 21
            __M_writer(str( venue.name ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 22
            __M_writer(str( venue.address ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 23
            __M_writer(str( venue.city ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 24
            __M_writer(str( venue.state ))
            __M_writer('</td>\n                <td>')
            # SOURCE LINE 25
            __M_writer(str( venue.zip_code ))
            __M_writer('                <td>\n                    <a href="/event/venues.edit/')
            # SOURCE LINE 26
            __M_writer(str( venue.id ))
            __M_writer('">Edit</a>\n                    |\n                    <a class="delete" href="/event/venues.delete/')
            # SOURCE LINE 28
            __M_writer(str( venue.id ))
            __M_writer('">Delete</a>\n                </td>\n            </tr>\n')
        # SOURCE LINE 32
        __M_writer('    </table>\n\n    <!-- Modal -->\n        <div id="delete_modal" class="modal fade" tabindex="-1" role="dialog">\n          <div class="modal-dialog" role="document">\n\n            <!-- Modal content-->\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title" id="MyModalLabel">Are You Sure?</h4>\n              </div>\n              <div class="modal-body">\n                <p>Delete the venue</p>\n              </div>\n              <div class="modal-footer">\n                <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n                <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n              </div>\n            </div>\n\n          </div>\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


