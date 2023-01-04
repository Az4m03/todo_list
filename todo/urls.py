from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, Login
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TodoList.as_view(), name='tasks'),
    path('task/<int:pk>/', TodoDetail.as_view(), name='task'),
    path('task-create', TodoCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TodoUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TodoDelete.as_view(), name='task-delete'),
]
