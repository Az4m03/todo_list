from django.http import HttpResponse
from django.shortcuts import render


def todoList(request):
    return HttpResponse('Hello world!')
