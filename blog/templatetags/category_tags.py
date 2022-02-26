from django import template
from blog.models import *

register = template.Library()




@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('category/categories_tags.html')
def get_categories():
    categories = Category.objects.all()
    return {"categories": categories}