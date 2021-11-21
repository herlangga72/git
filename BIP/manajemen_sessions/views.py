## IMPORTS

#guards
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#class builder
from rest_framework.views import APIView

#response
from rest_framework.response import Response
from rest_framework import status

# for sign off
from django.contrib.auth import logout

## END IMPORTS

#User Logoff and Much More


class LogoutView(APIView):

    def get(self, request):
    
        if not self.request.user.is_authenticated:
            return Response({'detail': 'You\'re not logged in.'},status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
        logout(request)        
    
        return Response({'detail': 'Successfully logged out.'})



# This for Guards 
class SessionView(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        return Response({ 'isAuthenticated': self.request.user.is_authenticated,})


class StaffView(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        return Response({ 'isStaff': self.request.user.is_staff,})

###########################


#user info

class WhoAmIView(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self ,request, format=None):

        data={
                'uuid'      : self.request.user.id ,
                'email'     : self.request.user.email,
                'username'  : f'{self.request.user.first_name} {self.request.user.last_name}',
                'avatar'    : self.request.user.avatar,
                'isAdmin'   : self.request.user.is_superuser,
                'isStaff'   : self.request.user.is_staff,
                'isPesertaPekerti': self.request.user.is_pekerti_peserta
            }
        return Response(data)
