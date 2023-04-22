from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from django.contrib.auth.forms import UsernameField, ReadOnlyPasswordHashField
from django import forms
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from backend.models import User, Group

__all__ = ['UserAdmin', 'GroupAdmin']

class UserForm(forms.ModelForm):
    username = UsernameField()
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format(reverse('admin:auth_user_password_change', kwargs={'id':self.instance.pk}))
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')


class UserAdmin(OldUserAdmin):
    fieldsets = (
        (None, {
          'fields': (
            'username', 
            'password'
          )
        }),
        (_('Information'), {
            "fields": (
                'first_name', 
                'last_name', 
                'email', 
            ),
        }),
        (_('Permissions'), {
            "fields": (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'user_permissions', 
                'groups'
            ),
        }),
        (_('Check'), {
            "fields": (
                'date_joined',
            ),
        }),
    )
    readonly_fields = (
        'username',
        'date_joined',
    )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'date_joined'
    )
    ordering = ('username', )
    search_fields = (
        'username', 
        'email'
    )
    filter_horizontal = ('user_permissions', )
    actions_on_top = True
    actions_on_bottom = True
    form = UserForm
    autocomplete_fields = (
        'groups', 
    )


class GroupAdmin(ModelAdmin):
    list_display = ('name', 'leader')
    search_fields = ('name', )
    autocomplete_fields = ('users', 'leader')
    readonly_fields = ('users',)