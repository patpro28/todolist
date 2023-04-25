from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from backend.models import User

__all__ = ['Project', 'ProjectMember']

class Project(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True, help_text=_("Slug will be used in the URL. Must be unique."))
    description = models.TextField(_('description'))
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    admins = models.ManyToManyField(User, verbose_name=_('admin'), related_name='admin_projects')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['-created_at']
        # permissions = [
        #     ('view_project', 'Can view project'),
        # ]
    

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('project'), related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='projects', on_delete=models.CASCADE)
    participation_time = models.DateTimeField(auto_now_add=True)
    # last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.job.title}'