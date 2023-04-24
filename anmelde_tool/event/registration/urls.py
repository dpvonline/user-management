from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register('registration', views.RegistrationViewSet, basename='registration')
router.register('registration-read', views.RegistrationReadViewSet, basename='registration')
router.register('my-registrations', views.MyRegistrationViewSet, basename='my-registrations')

registration_router = routers.NestedSimpleRouter(router, r'registration', lookup='registration')
registration_router.register(r'single-participant', views.RegistrationSingleParticipantViewSet,
                             basename='single-participant')
registration_router.register(r'group-participants', views.RegistrationGroupParticipantViewSet,
                             basename='group-participants')
registration_router.register(r'add-group-participants', views.RegistrationAddGroupParticipantViewSet,
                             basename='add-group-participants')
registration_router.register(r'attribute', views.RegistrationAttributeViewSet, basename='attribute')
registration_router.register(r'summary', views.RegistrationSummaryViewSet, basename='summary')
registration_router.register(r'workshop', views.WorkshopViewSet, basename='workshop')
registration_router.register(r'add-responsible', views.AddResponsiblePersonRegistrationViewSet, basename='add-responsible')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(registration_router.urls)),
]
