from django.contrib import admin
from .user import UserAdmin
from backend.models import User

admin.site.register(User, UserAdmin)