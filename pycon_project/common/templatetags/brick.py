from django import template

register = template.Library()


@register.filter
def start_row(value):
    """Check if the brick belongs a new row"""
    START = False
    if value < 3:
        START = (value - 1) % 3 == 0
    else:
        START = (value - 4) % 3 == 0
    return START


@register.filter
def end_row(value):
    """Check if it is the end of a row"""
    END = False
    if value < 3:
        END = (value - 1) % 3 == 2
    else:
        END = (value - 4) % 3 == 2
    return END
