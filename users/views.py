from django.shortcuts import render


def login(request):
    context = {'title': 'Cloneshop - Авторизация'}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'Cloneshop - Регистрация'}
    return render(request, 'users/registration.html', context)
