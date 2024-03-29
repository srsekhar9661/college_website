from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def small(dictionary, key):
    x = dictionary[key]
    return len(x) if isinstance(x, str) else x