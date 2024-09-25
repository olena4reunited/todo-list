from django import views
from django.shortcuts import render, redirect

from todo_app.forms import TaskForm
from todo_app.models import Task


class HomeView(views.View):
    template_name = "todo_app/index.html"

    def get(self, request):
        tasks = Task.objects.order_by("done", "-created_at")
        form = TaskForm()
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

