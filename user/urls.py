from django.urls import path

from . import views

urlpatterns = [
    path('/signup/', views.add_user, name='signup'),
    path('/login/', views.login, name='login'),
]
