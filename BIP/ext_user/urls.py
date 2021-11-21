#impot the view
from ext_user import views
from django.urls import path, include

# rest framework
from rest_framework import routers

# add models to routing  more simple
router = routers.DefaultRouter()
router.register('User', views.user_viewsets )

urlpatterns = [
    path('', include(router.urls)),
]