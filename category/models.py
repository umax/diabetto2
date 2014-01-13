# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

__all__ = (
    'Category',
)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('detail_category', kwargs={'pk': self.pk})
