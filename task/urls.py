from django.urls import path
from . import views

urlpatterns = [
    path('/<str:name>', views.tasks, name='tasks'),
    path('delete/<int:taskid>/<int:userid>/', views.deleteTask, name='deltask'),
    path('edit/<int:taskid>/<int:userid>/', views.edittask, name='edittask'),
]
