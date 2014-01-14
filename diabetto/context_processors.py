# -*- coding: utf-8 -*-

from django.conf import settings

__all__ = (
    'common',
)


def common(request):
    return {
        'settings': settings,
    }
