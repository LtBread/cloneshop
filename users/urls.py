from django.urls import path

from users.views import UserLoginView, UserRegistrationView, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')
]
