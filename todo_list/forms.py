from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control",
                       "rows": 2}
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "size": 5
                }
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter tag name"
                }
            ),
        }
