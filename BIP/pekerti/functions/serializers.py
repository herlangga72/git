from rest_framework import serializers
from pekerti.models import Peserta, Gelombang
from django.contrib.auth.models import User
from pekerti.functions.function import validate_file_extension

# this class not need a review  
class GelombangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gelombang
        fields = '__all__'
       
class PesertaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Peserta
        fields = '__all__'
