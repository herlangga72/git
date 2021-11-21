from rest_framework import serializers
from ext_user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_pekerti_peserta"]





# rest frameworks

from rest_framework import viewsets


#code

class user_viewsets(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset = User.objects.all()
    http_method_names=['patch']
 