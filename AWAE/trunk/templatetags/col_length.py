from django import template

register = template.Library()

@register.filter(name='col_length')
def col_length(value, arg):
    output = arg - value
    return output
