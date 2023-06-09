from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
)
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from backend.models import User
from backend.forms import UserLoginForm, UserRegisterForm

__all__ = [
    'UserLoginView', 
    'UserLogoutView', 
    'UserRegisterView',
    'UserListView',
    'UserDetailView',
    'UserUpdateView',
]

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    model = User
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        messages.success(self.request, _('Login success!'))
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, _('Login failed!'))
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(self.request, _('Logout success!'))
        return super().post(request, *args, **kwargs)


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'user/register.html'

    def get_success_url(self):
        return reverse('backend:login')

    def form_valid(self, form):
        messages.success(self.request, _('Register success!'))
        return super().form_valid(form)
    
class UserListView(ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'
    paginate_by = 20

class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'user'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/update.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'user'
    