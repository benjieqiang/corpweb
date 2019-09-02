# -*- coding: utf-8 -*-
# Author:benjamin
# Date:
from django import template

register = template.Library()

@register.filter
def my_filter(x,y):
    n1,n2 = y.split(',')
    if x % int(n1) == int(n2):
        return True
    else:
        return False

@register.filter
def t_filter(value,args):
    n1,n2 = args.split(',')
    if value % int(n1) == int(n2):
        return True
    return False