from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
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


class TodoCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TodoUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
