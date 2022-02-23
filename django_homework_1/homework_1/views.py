from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.


def greeting(request):
    return HttpResponse("<h1>Hello<h1>")


def introduction(request):
    text = "<h2>Page by Mikayel Muradyan</h2>"
    return HttpResponse(text)


def current_date_and_time(request):
    now = datetime.now()
    result = "<h2>Current date and time {}</h2>".format(now)
    return HttpResponse(result)


def task_with_dictionaries(request):
    dict_1 = dict()

    for i in range(1, 16):
        dict_1[i] = i ** 2

    res = "<h2>{}</h2>".format(dict_1)
    return HttpResponse(res)
