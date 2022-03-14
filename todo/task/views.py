from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from task.forms import TaskForm, TaskModelForms, TaskUpdateModelForm
from task.models import Task


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
    task_list = Task.objects.filter(user=request.user)

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
