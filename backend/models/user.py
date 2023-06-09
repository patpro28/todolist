from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

__all__ = ['User', 'Team']

class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Only English letters, numbers and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse('backend:detail', kwargs={'user': self.username})

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['username']


class Team(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='teams')
    leader = models.ForeignKey(User, related_name='leader_teams', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name