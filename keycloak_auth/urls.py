from django.urls import include, path
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register(r'group', views.AllGroupsViewSet, basename='group')

group_router = routers.NestedSimpleRouter(router, r'group', lookup='group')
group_router.register(r'members', views.GroupMembersViewSet, basename='members')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(group_router.urls)),
]
