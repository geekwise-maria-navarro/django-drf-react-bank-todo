from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, BranchSerializer
from .models import Todo, Branch

class TodoView(viewsets.ModelViewSet):       
    serializer_class = TodoSerializer          
    queryset = Todo.objects.all()

class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Branch.objects.all().order_by('id')
    serializer_class = BranchSerializer