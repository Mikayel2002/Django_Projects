from urllib.parse import urlparse
from django.urls import URLPattern, path
from task import views

urlpatterns = [
    path('', views.task_create, name="task_create"),
    path('tasks/', views.list_task, name="list_task"),
    path('tasks/<int:task_id>/', views.task_view, name="task_view"),
    path('tasks/<int:task_id>/update/', views.task_update, name="task_update"),
    path('tasks/<int:task_id>/delete/', views.task_delete, name="task_delete"),
]