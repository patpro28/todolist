from django.views.generic import (
  CreateView,
  UpdateView,
  ListView,
  DetailView,
)

from project.models import (
  Project,
  Todolist,
)

from project.forms import (
  ProjectForm,
)

__all__ = [
  'ProjectCreateView',
  'ProjectDetailView',
  # 'ProjectUpdateView',
  'ProjectListView',
  # 'TodolistCreateView',
  # 'TodolistUpdateView',
  # 'TodolistListView',
]

class ProjectCreateView(CreateView):
  model = Project
  form_class = ProjectForm
  template_name = 'project/create.html'

  def get_success_url(self):
    return reverse('project:detail', kwargs={'slug': self.object.slug})

  def form_valid(self, form):
    form.instance.admins.add(self.request.user)
    return super(ProjectCreateView, self).form_valid(form)


class ProjectDetailView(DetailView):
  model = Project
  template_name = 'project/detail.html'
  context_object_name = 'project'
  slug_field = 'slug'
  slug_url_kwarg = 'slug'


class ProjectListView(ListView):
  model = Project
  template_name = 'project/list.html'
  context_object_name = 'projects'
  paginate_by = 10