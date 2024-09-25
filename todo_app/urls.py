from django.urls import path

from todo_app.views import HomeView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagListView, TagCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="create-task"),
    path("<int:task_id>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("<int:task_id>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="create-tag"),
]

app_name = "todo-app"
