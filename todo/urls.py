from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('add-todo', views.add_todo, name='add-todo'),
    path('todo-delete', views.todo_delete, name='todo-delete'),
    path('todo-update/<str:title>', views.todo_update, name='todo-update')
]
