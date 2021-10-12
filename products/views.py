import datetime

from django.shortcuts import render


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
        'products': [
            {'img_src': '/static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'img_src': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face',
             'price': 23725,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'img_src': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'img_src': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': 2340,
             'description': 'Плотная ткань. Легкий материал.'},
            {'img_src': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'description': 'Гладкий кожаный верх. Натуральный материал.'},
            {'img_src': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}
        ]
    }
    return render(request, 'products/products.html', context)