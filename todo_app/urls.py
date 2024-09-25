from django.urls import path

from todo_app.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

app_name = "todo-app"
