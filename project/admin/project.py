from django.contrib import admin
from django import forms

from project.models import Project

__all__ = ['ProjectAdmin',]

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['owner'].queryset = User.objects.filter(is_staff=True)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('admins',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'slug')
    autocomplete_fields = ('admins',)
    form = ProjectAdminForm