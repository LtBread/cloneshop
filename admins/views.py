from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'CloneShop - Админ панель'}
    return render(request, 'admins/index.html', context)


# Create

class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-create.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Создание пользователей'
        return context


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'CloneShop - Создание пользователей', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# Read

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context


# @user_passes_test(lambda u: u.is_staff)s
# def admin_users(request):
#     context = {
#         'title': 'CloneShop - Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# Update

class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование пользователя'
        return context


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {
#         'title': 'CloneShop - Редактирование пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# Delete

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.save_delete()
        return HttpResponseRedirect(success_url)

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.save_delete()
#     return HttpResponseRedirect(reverse('admins:admin_users'))
