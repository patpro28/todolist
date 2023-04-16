from django.db import models
from backend.models import User

__all__ = ['Project', 'ProjectMember']

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, through='ProjectMember')
    admins = models.ManyToManyField(User, related_name='admin_projects')

    def __str__(self):
        return self.title
    

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.job.title}'