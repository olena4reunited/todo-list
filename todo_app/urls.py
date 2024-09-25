from django.urls import path

from todo_app.views import HomeView, TaskCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="create-task"),
]

app_name = "todo-app"
