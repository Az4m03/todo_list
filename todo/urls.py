from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate


urlpatterns = [
    path('', TodoList.as_view(), name='tasks'),
    path('task/<int:pk>/', TodoDetail.as_view(), name='task'),
    path('task-create', TodoCreate.as_view(), name='task-create'),
]
