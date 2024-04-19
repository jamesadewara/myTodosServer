from django.contrib import admin
from .models import Task, TaskDepartment
# Register your models here.
admin.site.register([
    Task,
    TaskDepartment
])