from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from BIP.settings import LOGIN_REDIRECT_URL

admin.site.site_url     =  LOGIN_REDIRECT_URL
admin.site.site_header  =  "Django Dashboard"  
admin.site.site_title   =  "BIP"
admin.site.index_title  =  "Biro Inovasi Pembelajaran"

app_url=[
    path('api/pekerti/'     , include ('pekerti.urls') ),
    path('api/users/'        , include ('ext_user.urls') ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







#########################################
#########################################
#########################################

frameworks=[ 
    path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('social_django.urls', namespace='social')),
]
auth_url=[ path('auth/'    , include ('manajemen_sessions.urls') ) ]
urlpatterns = frameworks  + app_url + auth_url #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #+ auth_url
# config loader



import configparser
from BIP.settings import BASE_DIR
config = configparser.ConfigParser()
config.read(BASE_DIR / 'config.ini')

# swagger 

if (config.getboolean('URL','IS_SWAGGER')):
    
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
    
    urlpatterns += [
        path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),    
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
    ]

#admin view
if (config.getboolean('URL','IS_ADMIN')):
    urlpatterns += [
        path('admin/'   , admin.site.urls ),
    ]