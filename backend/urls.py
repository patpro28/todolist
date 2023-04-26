from django.urls import path, include
from backend.views.user import *

app_name = 'backend'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='list'),
    path('detail/<str:user>/', include([
        path('', UserDetailView.as_view(), name='detail'),
        path('update/', UserUpdateView.as_view(), name='update'),
    ])),
]