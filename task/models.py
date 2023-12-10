from django.db import models
from user.models import user_info

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in progress', 'In Progress'),
        ('done', 'Done'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,default='low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
   

    def __str__(self):
        return f"{self.title}"


class Commends(models.Model):
    message=models.CharField( max_length=50)
    description = models.TextField(max_length=200)
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(user_info, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.message}"
