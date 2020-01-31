from django import template
import os
register = template.Library()


@register.filter
def get_filename(value):
    return os.path.split(value)[1]


@register.filter
def get_length(value):
    return len(value)
