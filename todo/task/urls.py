from urllib.parse import urlparse
from django.urls import URLPattern, path, include
from task.views import task as task_view
from task.views import task_api as task_api_view

urlpatterns = [
    path('', task_view.task_create, name="task_create"),
    path('tasks/', task_view.list_task, name="list_task"),
    path('tasks/<int:task_id>/', task_view.task_view, name="task_view"),
    path('tasks/<int:task_id>/update/', task_view.task_update, name="task_update"),
    path('tasks/<int:task_id>/delete/', task_view.task_delete, name="task_delete"),
    # path('api/', include('task.api.urls')),
]

class_view_urls = {
    path("tasks_class/", task_view.TaskListView.as_view(), name="task_class_list"),
    path("tasks_class/create", task_view.TaskCreateViewGeneric.as_view(), name="task_class_create"),
}

urlpatterns += class_view_urls

api_urls = {
    path('api/tasks/', task_api_view.TaskApiView.as_view()),
    path('api/tasks/<int:id>', task_api_view.TaskApiView.as_view()),
}

urlpatterns += api_urls
