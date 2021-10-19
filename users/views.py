from django.shortcuts import render

from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'CloneShop - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'CloneShop - Регистрация'}
    return render(request, 'users/registration.html', context)
