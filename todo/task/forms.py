import imp
from django import forms
from task.models import Task


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1256)

    def clean_name(self):
        _name = self.cleaned_data["name"]

        # if Task.objects.filter(name=_name).exists():
        if len(Task.objects.filter(name=_name)) > 1:
            # raise forms.ValidationError("Task already exists")
            raise forms.ValidationError("there are alredyntwo with this name")

        print(_name, "###")
        return _name


class TaskModelForms(forms.ModelForm):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = ("name", "description", "status")
        # exclude = ("name", "description", "status")


class TaskUpdateModelForm(forms.ModelForm):

    def clean_name(self):
        _name = self.cleaned_data["name"]

        # if Task.objects.filter(name=_name).exists():
        if len(Task.objects.filter(name=_name)) > 1:
            # raise forms.ValidationError("Task already exists")
            raise forms.ValidationError("there is already a task with this name")

        return _name

    class Meta:
        model = Task
        fields = ("name", "description", "status")
