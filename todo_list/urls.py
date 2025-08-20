from django.urls import path
from todo_list import views

urlpatterns = [
    path("", views.index, name="index"),
    path("task/add/", views.task_create, name="task-add"),
    path("task/<int:pk>/update/", views.task_update, name="task-update"),
    path("task/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("task/<int:pk>/toggle/", views.toggle_task, name="task-toggle"),
    path("tags/", views.tag_list, name="tag-list"),
    path("tags/add/", views.tag_create, name="tag-add"),
    path("tags/<int:pk>/update/", views.tag_update, name="tag-update"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag-delete"),
]
