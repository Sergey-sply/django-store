from django import template

from carts.utils import get_user_carts

register = template.Library()

@register.simple_tag()
def user_carts(request):
    """Takes all carts of this user"""
    return get_user_carts(request)
    
