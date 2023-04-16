from django.contrib import admin
from django import forms

from project.models import Todolist

__all__ = ['TodolistAdmin']

class TodolistAdminForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ('title', 'description', 'user')

class TodolistAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'user')
    list_filter = ('user',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'user')
    form = TodolistAdminForm