from django import template
from django.db.models import Count, F

from ..models import Category

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cn=Count('news', filter=F('news__is_published')))
    return {"categories": categories}
