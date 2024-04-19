from django.db import models
from django.utils.html import mark_safe
from datetime import timezone

class TaskDepartment(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="thumbnail/img/group/")
    background_color = models.CharField(max_length=150)
    foreground_color = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Task(models.Model):
    user_email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    group = models.ForeignKey(TaskDepartment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.title