# -*- coding: utf-8 -*-

from django.forms import ModelForm
from category.models import Category

__all__ = (
    'CategoryForm',
)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages = {
            'required': u'Название группы не может быть пустым',
        }
