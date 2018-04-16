from django import template
register = template.Library()

@register.filter
def get_sum(List, i):
    return List[int(i)].get('amount__sum')