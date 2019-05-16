from rest_framework import serializers

from .models import User,User_Joined_Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail','phone')

class User_Joined_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Joined_Group
        fields = ('name', 'user')
