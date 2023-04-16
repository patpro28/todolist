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

from backend.models import User
from backend.forms import UserLoginForm

__all__ = []

class UserLoginView(LoginView):
    template_name = 'backend/login.html'
    model = User
    authentication_form = UserLoginForm
    
class UserLogoutView(LogoutView):
    pass