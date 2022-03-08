from django import forms
from django.core.exceptions import ValidationError

from task.models import Task


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1256)

    def clean_name(self):
        _name = self.cleaned_data["name"]

        # if Task.objects.filter(name=_name).exists():
        #     raise ValidationError("Task already exists")
        #
        # return _name

        if len(Task.objects.filter(name=_name)) > 1:
            raise ValidationError("There are two tasks with this name")

        return _name


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ("name", "description", "status")
        # exclude = ("name", "description")
        fields = "__all__"
