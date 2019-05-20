import django_filters
from rest_framework import viewsets,filters

from .models import User,User_Joined_Group,User_Has_Task,Group,Group_Has_Member,Task
from .serializer import UserSerializer,User_Joined_GroupSerializer,User_Has_TaskSerializer,GroupSerializer,Group_Has_MemberSerializer,TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_Joined_GroupViewSet(viewsets.ModelViewSet):
    queryset = User_Joined_Group.objects.all()
    serializer_class = User_Joined_GroupSerializer

class User_Has_TaskViewSet(viewsets.ModelViewSet):
    queryset = User_Has_Task.objects.all()
    serializer_class = User_Has_TaskSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Group_Has_MemberViewSet(viewsets.ModelViewSet):
    queryset = Group_Has_Member.objects.all()
    serializer_class = Group_Has_MemberSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
