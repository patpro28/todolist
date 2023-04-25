from django.urls import path

from project.views.project import *

app_name = 'project'

urlpatterns = [
  path('create/', ProjectCreateView.as_view(), name='create'),
  path('detail/<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
  path('list/', ProjectListView.as_view(), name='list'),
]