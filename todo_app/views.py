from django import views
from django.shortcuts import render, redirect, get_object_or_404

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class HomeView(views.View):
    template_name = "todo_app/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, pk=task_id)
            task.done = not task.done
            task.save()
            return redirect("todo-app:home")

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
            return redirect("todo-app:home")
        return render(request, self.template_name, {'form': form})



class TaskUpdateView(views.View):
    template_name = "todo_app/task_form.html"

    def get(self, request, task_id):
        form = TaskForm(instance=Task.objects.get(pk=task_id))
        return render(request, self.template_name, {'form': form})

    def post(self, request, task_id):
        form = TaskForm(request.POST, instance=Task.objects.get(pk=task_id))
        if form.is_valid():
            form.save()
            return redirect("todo-app:home")
        return render(request, self.template_name, {'form': form})



class TaskDeleteView(views.View):
    template_name = "todo_app/task_delete_confirmation.html"

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect("todo-app:home")


class TagListView(views.View):
    template_name = "todo_app/tag_list.html"

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, self.template_name, {'tags': tags})
