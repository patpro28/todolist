from django.contrib import admin
from .user import *
from backend.models import User, Team

admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)