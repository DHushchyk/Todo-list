from django.urls import path

from tasks.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    confirm_undo_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("/create/", TaskCreateView.as_view(), name="task-create"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("/tags/", TagListView.as_view(), name="tag-list"),
    path("/tags/create/", TagCreateView.as_view(), name="task-create"),
    path("/tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("/tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("/<int:pk>/confirm_undo_task/", confirm_undo_task, name="confirm-undo-task")
]

app_name = "tasks"
