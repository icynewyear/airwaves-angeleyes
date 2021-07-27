from django import template

register = template.Library()

@register.filter(name='col_length')
def col_length(value, arg):
    if value == 1:
        output = arg
    elif arg == value:
        output = 1
    else:
        output = arg - value
    if output == 0:
        output = 1
    return output
