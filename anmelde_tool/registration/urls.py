from django.urls import include, path
from rest_framework_nested import routers
from anmelde_tool.registration import views

router = routers.SimpleRouter()
router.register('registration', views.RegistrationViewSet, basename='registration')
router.register('registration-read', views.RegistrationReadViewSet, basename='registration')
router.register('my-registrations', views.MyRegistrationViewSet, basename='my-registrations')

registration_router = routers.NestedSimpleRouter(router, r'registration', lookup='registration')
registration_router.register(
    r'single-participant', views.RegistrationSingleParticipantViewSet,
    basename='single-participant'
)
# registration_router.register(
#     r'group-participants', views.RegistrationGroupParticipantViewSet,
#     basename='group-participants'
#     )
# registration_router.register(
#     r'add-group-participants', views.RegistrationAddGroupParticipantViewSet,
#     basename='add-group-participants'
#     )
registration_router.register(r'boolean-attribute', views.RegistrationBooleanAttributeViewSet,
                             basename='boolean-attribute')
registration_router.register(r'string-attribute', views.RegistrationStringAttributeViewSet, basename='string-attribute')
registration_router.register(r'travel-attribute', views.RegistrationTravelAttributeViewSet, basename='travel-attribute')
registration_router.register(r'float-attribute', views.RegistrationFloatAttributeViewSet, basename='float-attribute')
registration_router.register(r'time-attribute', views.RegistrationTimeAttributeViewSet, basename='time-attribute')
registration_router.register(r'integer-attribute', views.RegistrationIntegerAttributeViewSet,
                             basename='integer-attribute')
registration_router.register(r'summary', views.RegistrationSummaryViewSet, basename='summary')

registration_router.register(
    r'add-responsible',
    views.AddResponsiblePersonRegistrationViewSet,
    basename='add-responsible'
)

registration_router.register(r'send-confirmation-mail', views.SendConfirmationMail,
                             basename='send-confirmation-mail')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(registration_router.urls)),
]
