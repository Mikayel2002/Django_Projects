from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

import task
from task.forms import TaskForm, TaskModelForms, TaskUpdateModelForm
from task.models import Task
from django.views.generic import (
    View,
    ListView,
    UpdateView,
    DetailView,
    CreateView,
    DeleteView
)


# class TaskListView(View):
#     def get(self, request):
#         task_list = Task.objects.all()
#
#         context = {"task_list": task_list}
#
#         return render(request, "task/index_class.html", context)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/index_class.html"
    ordering = "-created_at"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def get_ordering(self):
        order_var = self.request.GET.get("order_by")

        if order_var:
            return order_var

        return super().get_ordering()


# class TaskCreateView(LoginRequiredMixin, View):
#     model = Task
#     template_name = "task/new_task_class.html"
#     success_url = "task_class_list"
#     form_class = TaskModelForms
#
#     def get(self, request):
#         form = self.form_class()
#         context = {"task_form": form}
#
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#             messages.success(request, "Created")
#             return redirect(self.success_url)
#
#         messages.success(request, "Failed")
#         return redirect("task_class_create")


class TaskCreateViewGeneric(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskModelForms
    template_name = "task/new_task_class.html"
    success_url = "/tasks_class"


# @login_required(login_url="user_login")
# def task_create(request):
#     form = TaskForm()
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#
#             task = Task.objects.create(**form.cleaned_data, user=request.user)
#
#             return redirect("task_view", task_id=task.id)
#
#     context = {"form": form}
#
#     return render(request, "task/new_task.html", context)


@login_required(login_url="user_login")
def task_create(request):
    form = TaskModelForms()

    if request.method == "POST":
        form = TaskModelForms(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f"task {task.name} was created successfully")
            
            return redirect("task_view", task_id=task.id)

    context = {"form": form}

    return render(request, "task/new_task.html", context)


@login_required(login_url="user_login")
def list_task(request):
    # task_list = Task.objects.filter(user=request.user)
    query_string = request.GET.get("search_task")
    if query_string:
        task_list = request.user.task_set.filter(name__contains=query_string)
    else:
        task_list = request.user.task_set.all()

    return render(request, "task/index.html", context={"tasks": task_list})    


@login_required(login_url="user_login")
def task_view(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        return redirect("list_task")
    return render(request, "task/task_view.html", context={"task_object": task}) 


@login_required(login_url="user_login")
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    form = TaskUpdateModelForm(instance=task)

    if request.method == "POST":
        form = TaskUpdateModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"task {task.name} was updated successfully")

            return redirect("task_view", task_id=task.id)

    context = {
        "task_object": task,
        "form": form
    }
    return render(request, "task/task_update.html", context)


@login_required(login_url="user_login")
def task_delete(request, task_id):
    try:
        Task.objects.get(id=task_id, user=request.user).delete()
    except Task.DoesNotExist:
        pass

    return redirect("list_task")
