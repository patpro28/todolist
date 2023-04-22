from django.contrib import admin
from .todolist import *
from .project import *
from project.models import Todolist, Project, ProjectMember

# Register your models here.

admin.site.register(Todolist, TodolistAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMember)