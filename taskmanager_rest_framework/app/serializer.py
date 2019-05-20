from rest_framework import serializers

from .models import User,User_Joined_Group,User_Has_Task,Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail','phone')

class User_Joined_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Joined_Group
        fields = ('group', 'user')

class User_Has_TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Has_Task
        fields = ('task_name', 'user','comment')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
