from django.contrib import admin
from .user import *
from backend.models import User, Group

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)