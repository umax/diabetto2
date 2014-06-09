# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

__all__ = (
    'Category',
)

class Category(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        error_messages={'unique': u'Группа с таким названием уже существует'})

    class Meta:
        ordering = ['name']
        verbose_name = u'Группа продуктов'
        verbose_name_plural = u'группы продуктов'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_category', kwargs={'pk': self.pk})

    def admin_category_name(self):
        return self.name
    admin_category_name.short_description = u'Название'

    def admin_products_count(self):
        return self.product_set.all().count()
    admin_products_count.short_description = u'Количество продуктов'
