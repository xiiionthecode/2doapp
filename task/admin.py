from django.contrib import admin
from .models import Task, Commends

class Task_Admin(admin.ModelAdmin):
    list_display = ['id', 'title']
admin.site.register(Task, Task_Admin)

class Commends_Admin(admin.ModelAdmin):
    list_display = ['id', 'message']
admin.site.register(Commends, Commends_Admin)