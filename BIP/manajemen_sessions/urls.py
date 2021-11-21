from django.urls import path, include
from .views import SessionView, WhoAmIView, LogoutView, StaffView

urlpatterns = [
    path('sign/out/',LogoutView.as_view(), name='api-logout'),
    path('session/', SessionView.as_view(),name='api-session'),
    path('staff/'  , StaffView.as_view(),  name='api-staff'),
    path('whoami/',  WhoAmIView.as_view(), name='api-whoami'),
]
