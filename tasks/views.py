from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone


# GET /tasks/
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# GET /tasks/<id>/ and DELETE /tasks/<id>/
class TaskDetailView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskForkView(APIView):
    def post(self, request, pk):
        original_task = get_object_or_404(Task, pk=pk)
        
        forked_task = Task.objects.create(
            name=f"{original_task.name} (Forked)",
            type=original_task.type,
            created_at=timezone.now()  # optional
        )
        serializer = TaskSerializer(forked_task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)