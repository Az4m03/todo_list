from django.urls import path
from . import views


urlpatterns = [
    path('', views.todoList, name='tasks')
]