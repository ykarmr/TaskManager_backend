from rest_framework import routers
from .views import UserViewSet,User_Joined_GroupViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('user_joined_groups', User_Joined_GroupViewSet)
