from django.urls import path
from .views import (
  TaskListCreateView,
  TaskDetailView,
  TaskUpdateView,
  RemoveTaskView,
  TaskDepartmentDetailView,
  TaskDepartmentListCreateView
)

urlpatterns = [
    path('task/', TaskListCreateView.as_view(), name='Task-list-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='Task-detail'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='Task-update'),
    path('task/remove/<int:pk>/', RemoveTaskView.as_view(), name='remove-task'),
    path('task-departments/', TaskDepartmentListCreateView.as_view(), name='task-department-list-create'),
    path('task-department/<int:pk>/', TaskDepartmentDetailView.as_view(), name='task-department-detail'),
]