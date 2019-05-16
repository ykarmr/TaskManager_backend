import django_filters
from rest_framework import viewsets,filters

from .models import User,User_Joined_Group
from .serializer import UserSerializer,User_Joined_GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_Joined_GroupViewSet(viewsets.ModelViewSet):
    queryset = User_Joined_Group.objects.all()
    serializer_class = User_Joined_GroupSerializer
