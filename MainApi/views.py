# views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Task, TaskDepartment
from .serializers import TaskSerializer, TaskDepartmentSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  # Require authentication for creating tasks
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        # Set the user_email field with the authenticated user's email
        serializer.save(user_email=self.request.user.email)

class TaskDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RemoveTaskView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskDepartment.objects.all()
    serializer_class = TaskDepartmentSerializer

class TaskDepartmentDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskDepartment.objects.all()
    serializer_class = TaskDepartmentSerializer
