#import model dan serializer
from pekerti.models import Peserta, Gelombang
from pekerti.functions.serializers import PesertaSerializer, GelombangSerializer

# rest frameworks
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# premission
from pekerti.functions.permission import UserPermission,GelombangPermission

# filtering 
from django_filters import rest_framework as filters



# code

# Advanced filtering Using Django Filters
class GelombangFilter(filters.FilterSet):
    date_start = filters.DateFilter(field_name="start_date", lookup_expr='gte')
    date_end = filters.DateFilter(field_name="end_date", lookup_expr='lte')

    class Meta:
        model = Gelombang
        fields = ['date_start','date_end']

class PesertaFilter(filters.FilterSet):
    gelombang = filters.NumberFilter(field_name="gelombang")
    owner = filters.CharFilter(field_name="owner__email")
    is_validated = filters.CharFilter(field_name="is_validated")
    nama = filters.CharFilter(field_name="nama", lookup_expr="contains")
    nidn = filters.CharFilter(field_name="nidn")
    institusi_asal = filters.CharFilter(field_name="institusi_asal")
    class Meta:
        model = Peserta
        fields = ['gelombang','owner','is_validated','nama','nidn','institusi_asal']


# ModelVIew Set
class peserta_viewsets(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    filterset_class = PesertaFilter
    # filterset_fields = 
    permission_classes = [UserPermission]
    serializer_class=PesertaSerializer
    queryset = Peserta.objects.all()
    http_method_names=['get','post','patch','delete']

class gelombang_viewset(viewsets.ModelViewSet):
    
    filterset_class = GelombangFilter
    permission_classes = [GelombangPermission]
    serializer_class = GelombangSerializer
    queryset = Gelombang.objects.all()
    http_method_names=['get','post','patch','delete']
