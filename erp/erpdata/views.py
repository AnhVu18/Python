from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import PartSerializer, UserSerializer, ProjectSerializer, StageSerializer, CategorysSerializer, WorkSerializer
from .models import User, Part, Categorys, Comment, CostOfWork, Document, ExtraWork, Process, Project, SampleDoc, Role, SampleStep, Stage, Work 


class PartViewSet(viewsets.ModelViewSet):
     queryset = Part.objects.all()
     serializer_class = PartSerializer
     # permission_classes = [permissions.IsAuthenticated]

     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()]

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()]

class ProjectViewSet(viewsets.ModelViewSet):
     queryset = Project.objects.all()
     serializer_class = ProjectSerializer
     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()]

class StageViewSet(viewsets.ModelViewSet):
     queryset = Stage.objects.all()
     serializer_class = StageSerializer
     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()]
  
class CategorysViewSet(viewsets.ModelViewSet):
     queryset = Categorys.objects.all()
     serializer_class = CategorysSerializer
     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()]
     
class WorkViewSet(viewsets.ModelViewSet):
     queryset = Work.objects.all()
     serializer_class = WorkSerializer
     def get_permissions(self):
          if self.action == 'list':
               return [permissions.AllowAny()]
          return [permissions.IsAuthenticated()] 







def index(request):
     return HttpResponse("Hello")





