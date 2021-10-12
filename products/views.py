import os
import datetime
import json

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'CloneShop',
        'user': 'илья',
        'now': datetime.datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'CloneShop - Каталог',
        'user': 'илья',
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
