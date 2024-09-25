from django import views
from django.shortcuts import render, redirect

from todo_app.forms import TaskForm
from todo_app.models import Task


class HomeView(views.View):
    template_name = "todo_app/index.html"

    def dispatch(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("done", "-created_at")
        return render(request, self.template_name, {'tasks': tasks})



class TaskCreateView(views.View):
    template_name = "todo_app/task_form.html"

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

