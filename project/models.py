from django.db import models
from django.utils.translation import gettext_lazy as _
from backend.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(_('project name'), max_length=255)
    description = models.TextField(_('description'))
    major = models.ForeignKey(User, verbose_name=_('team leader'), related_name='project', on_delete=models.SET_NULL)
    members = models.ManyToManyField(User, through='MemberProject')


class TodoList(models.Model):
    STATUS = (
        ('f', 'Finish'),
        ('p', 'In progress')
    )

    user = models.ForeignKey(User, verbose_name=_('user'), related_name='todolist', on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, verbose_name=_("project"), related_name='project_jobs', on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    status = models.CharField(_('status'), choices=STATUS, max_length=1)
    date = models.DateTimeField(_('date created'), auto_now_add=True)
    deadline = models.DateTimeField(_('deadline'), blank=True, null=True)

    class Meta:
        verbose_name = _('todo list')
        verbose_name_plural = _('todo lists')

    def __str__(self) -> str:
        return f'{self.user} - {self.title}'


class MemberProject(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='projects', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name=_("project"), related_name='project_members', on_delete=models.CASCADE)
