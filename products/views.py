import datetime
from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'CloneShop',
        'now': datetime.datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'CloneShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
