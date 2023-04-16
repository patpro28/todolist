from django.contrib import admin
from .todolist import *
from project.models import Todolist

# Register your models here.

admin.site.register(Todolist, TodolistAdmin)