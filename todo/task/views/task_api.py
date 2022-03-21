from task.models import Task
from rest_framework.response import Response
from task.serializers import TaskSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


@api_view(["GET", "POST", "PUT"])
# @renderer_classes([JSONRenderer])
def get_tasks(request):
    task_list = Task.objects.all()
    serialized_objects = TaskSerializer(task_list, many=True)

    return Response(serialized_objects.data)


class TaskApiView(APIView):
    def get(self, request):
        task_list = Task.objects.all()
        serialized_objects = TaskSerializer(task_list, many=True)

        return Response(serialized_objects.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response(serializer.data)
