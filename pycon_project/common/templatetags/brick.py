from django import template

register = template.Library()

@register.filter
def start_row(value):
    """Removes all values of arg from the given string"""
    return (value - 1) % 3 == 0

@register.filter
def end_row(value):
    """Removes all values of arg from the given string"""
    return (value - 1) % 3 == 2
