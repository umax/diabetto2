# -*- coding: utf-8 -*-

from django.db import models

__all__ = (
    'Product',
)


class Product(models.Model):
    name = models.CharField(max_length=128)
