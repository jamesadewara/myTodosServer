from rest_framework import serializers
from .models import Task, TaskDepartment

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDepartment
        fields = '__all__'