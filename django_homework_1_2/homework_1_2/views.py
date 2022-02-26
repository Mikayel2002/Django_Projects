from django.shortcuts import render, HttpResponse
import json

# Create your views here.


def reading_json_file(request):
    with open("info.json") as json_file:
        data = json.load(json_file)

    return HttpResponse(data)
