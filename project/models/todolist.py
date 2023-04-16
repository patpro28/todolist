from django.db import models

__all__ = ['Todolist']

class Todolist(models.Model):
    STATUS = (
        ('f', 'Finish'),
        ('p', 'In progress'),
        ('s', 'Suspense')
    )

    user = models.ForeignKey('backend.User', related_name='todolists', on_delete=models.CASCADE)
    project = models.ForeignKey('project.Project', related_name='todolists', on_delete=models.CASCADE)
    creator = models.ForeignKey('backend.User', related_name='created_todolists', on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=1)

    def __str__(self):
        return self.title