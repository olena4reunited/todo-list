from django import views
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from todo_app.forms import TaskForm, TagForm
from todo_app.models import Task, Tag


class HomeView(views.View):
    template_name = "todo_app/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, pk=task_id)
            task.done = not task.done
            task.save()
            return redirect("todo-app:home")

        tasks = Task.objects.order_by("done", "-created_at")
        return render(request, self.template_name, {"tasks": tasks})


class BaseFormView(views.View):
    form_class = None
    template_name = None
    success_url = None
    model = None

    def get_object(self):
        return None

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        return render(
            request,
            self.template_name,
            {"form": form, "is_update": bool(self.get_object())}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(
            request,
            self.template_name,
            {"form": form, "is_update": bool(self.get_object())}
        )


class TaskCreateView(BaseFormView):
    template_name = "todo_app/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo-app:home")


class TaskUpdateView(BaseFormView):
    template_name = "todo_app/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo-app:home")
    model = Task

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs["task_id"])


class TaskDeleteView(views.View):
    template_name = "todo_app/task_delete_confirmation.html"

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, self.template_name, {"task": task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect("todo-app:home")


class TagListView(views.View):
    template_name = "todo_app/tag_list.html"

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, self.template_name, {"tags": tags})


class TagCreateView(BaseFormView):
    template_name = "todo_app/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("todo-app:tag-list")


class TagUpdateView(BaseFormView):
    template_name = "todo_app/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("todo-app:tag-list")
    model = Tag

    def get_object(self):
        return get_object_or_404(
            Tag,
            pk=self.kwargs["tag_id"]
        )


class TagDeleteView(views.View):
    template_name = "todo_app/tag_delete_confirmation.html"

    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, pk=tag_id)
        return render(request, self.template_name, {"tag": tag})

    def post(self, request, tag_id):
        tag = get_object_or_404(Tag, pk=tag_id)
        tag.delete()
        return redirect("todo-app:tag-list")
