# -*- coding: utf-8 -*-

from django.forms import ModelForm, ValidationError
from product.models import Product

__all__ = (
    'ProductForm',
)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'carbohydrates', 'glycemic_index']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': u'Название продукта не может быть пустым',
        })
        self.fields['carbohydrates'].error_messages.update({
            'required': u'Количество углеводов не может быть пустым',
            'invalid': u'Неверное значение',
        })
        self.fields['glycemic_index'].error_messages.update({
            'required': u'Гликемический индекс не может быть пустым',
            'invalid': u'Неверное значение',
        })

    def clean_carbohydrates(self):
        carbohydrates = self.cleaned_data.get('carbohydrates')
        if carbohydrates == 0:
            raise ValidationError(u'Количество углеводов не может быть 0')

        return carbohydrates
