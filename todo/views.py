from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TodoList(ListView):
    model = Task
    context_object_name = 'tasks'


class TodoDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
