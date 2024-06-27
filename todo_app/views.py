from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer


class TodosView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
