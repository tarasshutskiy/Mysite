from django import template

from blog.models import Category

register = template.Library()




@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return Category.objects.all()







