# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

__all__ = (
    'Product',
)


class Product(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('detail_product', kwargs={'pk': self.pk})
