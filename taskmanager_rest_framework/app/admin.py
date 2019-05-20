from django.contrib import admin

# Register your models here.
from .models import User,User_Joined_Group,User_Has_Task,Group

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(User_Joined_Group)
class User_Joined_GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(User_Has_Task)
class User_Has_TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
