from django.urls import path
from backend.views.user import UserLoginView, UserLogoutView

app_name = 'backend'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]