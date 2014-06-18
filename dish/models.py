# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

__all__ = (
    'Dish',
)

class Dish(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        error_messages={'unique': u'Блюдо с таким названием уже существует'})
    portions = models.PositiveIntegerField(default=2)

    class Meta:
        ordering = ['name']
        verbose_name = u'Блюдо'
        verbose_name_plural = u'блюда'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_dish', kwargs={'pk': self.pk})