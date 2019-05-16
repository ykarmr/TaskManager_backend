from django.contrib import admin

# Register your models here.
from .models import User,User_Joined_Group

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(User_Joined_Group)
class User_Joined_GroupAdmin(admin.ModelAdmin):
    pass
