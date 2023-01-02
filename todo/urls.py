from django.urls import path
from .views import TodoList, TodoDetail


urlpatterns = [
    path('', TodoList.as_view(), name='tasks'),
    path('task/<int:pk>/', TodoDetail.as_view(), name='task'),
]
