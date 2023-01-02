from django.shortcuts import render
from django.views.generic import ListView
from .models import Task


class TodoList(ListView):
    model = Task
    context_object_name = 'tasks'
