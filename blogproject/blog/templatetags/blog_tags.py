from ..models import Port,Category,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Port.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Port.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('port')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('port')).filter(num_posts__gt=0)