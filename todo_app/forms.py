from django import forms
from django.utils import timezone

from todo_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date", "title": "Deadline"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None:
            self.fields["done"].initial = False

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline is not None and deadline < timezone.now():
            raise forms.ValidationError("Deadline must be in the future")
        return deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
