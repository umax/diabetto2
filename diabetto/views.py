# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView)

from diabetto import models

__all__ = (
    'IndexView',

    'ProductIndexView',
    'ProductDetailView',
    'ProductCreateView',
)

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        return self.render_to_json_response(form.errors, status=400)

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        data = {'pk': self.object.pk}
        return self.render_to_json_response(data, status=200)


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductIndexView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'index_product.html'


class ProductDetailView(DetailView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'detail_product.html'


class ProductCreateView(AjaxableResponseMixin, CreateView):
    model = models.Product
    fields = ['name']
    success_url = reverse_lazy('index_product')
