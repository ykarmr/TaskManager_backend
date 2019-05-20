from rest_framework import routers
from .views import UserViewSet,User_Joined_GroupViewSet,User_Has_TaskViewSet,GroupViewSet,Group_Has_MemberViewSet,TaskViewSet


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('user_joined_groups',User_Joined_GroupViewSet)
router.register('user_has_tasks',User_Has_TaskViewSet)
router.register('groups',GroupViewSet)
router.register('group_has_members',Group_Has_MemberViewSet)
router.register('tasks',TaskViewSet)
