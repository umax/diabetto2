# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse

__all__ = (
    'AjaxableResponseMixin',
)


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context={}, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        return self.render_to_json_response(form.errors, status=400)

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        return self.render_to_json_response({}, status=200)
