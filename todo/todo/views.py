from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.serializers import ToDoSerializer
from todo.models import ToDo
from django.shortcuts import get_object_or_404

class ToDoListView(APIView):

	def get(self, request):
		todos = ToDo.objects.all()
		serializer = ToDoSerializer(todos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ToDoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):

	def get(self, request, pk):
		todo = get_object_or_404(ToDo, pk=pk)
		serializer = ToDoSerializer(todo)
		return Response(serializer.data)

	def put(self, request, pk):
		todo = get_object_or_404(ToDo, pk=pk)
		serializer = ToDoSerializer(todo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		todo = get_object_or_404(ToDo, pk=pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
