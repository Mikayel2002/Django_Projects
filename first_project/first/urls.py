from django.urls import path
from first import views

urlpatterns = [
    path('a/', views.home),
    path('create_task/', views.create_task),
    path('tasks/', views.list_tasks),
    path('task_filter/', views.task_filter),
]
