from rest_framework import serializers

from .models import User,User_Joined_Group,User_Has_Task,Group,Group_Has_Member,Task

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

class Group_Has_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_Has_Member
        fields = ('group','user')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title',)
