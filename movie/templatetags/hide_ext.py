from django import template

register = template.Library()

@register.filter
def hide_ext(value):
    return value.replace(".webm","")
