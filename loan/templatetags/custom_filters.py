from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, "")


@register.filter
def is_equal(exp1, exp2):
    return exp1 == exp2
