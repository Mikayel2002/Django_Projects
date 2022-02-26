from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from first.models import Task

# Create your views here.


def home(request):
    data = {"a": 5}
    return HttpResponse("Hello django world {}".format(data))


def create_task(request):
    # TODO take the values from html
    task_name = "python 3"
    description = "look into docs"
    status = 2

    # task = Task(name=task_name, description=description, status=status)
    # task.save()

    task = Task.objects.create(name=task_name, description=description, status=status)

    return HttpResponse("Success! {}".format(task))


def list_tasks(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(status=2)
    print(tasks)
    response = ""
    for i in tasks:
        response += str(i) + "<br>"

    # print(request.__dict__)
    print(request.GET)

    return HttpResponse(response)


def task_filter(request):
    # try:
    #     name = request.GET["name"]
    # except MultiValueDictKeyError:
    #     name = ""

    name = request.GET.get("name", None)

    if name:
        response = Task.objects.filter(name=name)
    else:
        response = Task.objects.all()

    return HttpResponse(response)
