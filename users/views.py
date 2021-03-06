import django.contrib.auth.backends
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from users.models import User, UserProfile
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserExtendedProfileForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'CloneShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request,
                                 'Вам отправлено письмо. Для подтверждения регистрации пройдите по ссылке в письме.')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Ошибка регистрации!')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'CloneShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


@transaction.atomic
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        form_extended = UserExtendedProfileForm(instance=user.userprofile, data=request.POST)
        if form.is_valid() and form_extended.is_valid():
            form.save()
            form_extended.save()
            messages.success(request, 'Данные успешно изменены!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
        form_extended = UserExtendedProfileForm(instance=user.userprofile)
    context = {
        'title': 'CloneShop - Профиль',
        'form': form,
        'form_extended': form_extended,
        'baskets': Basket.objects.filter(user=user)
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учётной записи {user.username}'
    message = f'Для подтверждения учётной записи {user.username} на портале ' \
              f'{settings.DOMAIN_NAME} перейдите по ссылке {settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.BaseBackend')
            return render(request, 'users/verification.html')
        else:
            print(f'ERROR ACTIVATION USER {user.username}')
            return render(request, 'users/verification.html')
    except Exception as e:
        print(f'error activation user {e.args}')
        return HttpResponseRedirect(reverse('index'))
