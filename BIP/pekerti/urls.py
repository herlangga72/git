#impot the view
from pekerti import views
from django.urls import path, include

# rest framework
from rest_framework import routers

# add models to routing  more simple
router = routers.DefaultRouter()
router.register('peserta', views.peserta_viewsets)
router.register('gelombang', views.gelombang_viewset)

urlpatterns = [
    path('', include(router.urls)),
]