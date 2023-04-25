from django import forms
from django_ace import AceWidget
from project.models import Project, ProjectMember

__all__ = ['ProjectForm', 'ProjectMemberForm']

class ProjectForm(forms.ModelForm):
  description = forms.CharField(widget=AceWidget(mode='markdown', theme='monokai', width='100%', height='300px'))
  class Meta:
    model = Project
    fields = [
      'title',
      'description',
    ]
