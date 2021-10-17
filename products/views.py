import os
import datetime
import json

from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'CloneShop',
        'user': 'илья',
        'now': datetime.datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'CloneShop - Каталог',
        'user': 'илья',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
