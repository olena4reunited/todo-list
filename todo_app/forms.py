from django import forms
from django.utils import timezone

from todo_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date", "title": "Deadline"}
            ),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < timezone.now():
            raise forms.ValidationError("Deadline must be in the future")
        return deadline

