from django.urls import path

from todo_app.views import HomeView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="create-task"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
]

app_name = "todo-app"
