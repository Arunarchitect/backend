from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.db.models import Q
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        client_name = self.request.query_params.get('client_name', None)
        location = self.request.query_params.get('location', None)
        project_type = self.request.query_params.get('project_type', None)

        if client_name:
            queryset = queryset.filter(Q(client_name__icontains=client_name))
        if location:
            queryset = queryset.filter(Q(location__icontains=location))
        if project_type:
            queryset = queryset.filter(Q(project_type__icontains=project_type))

        return queryset

    def get_serializer_class(self):
        return ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
