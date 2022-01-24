from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from django.conf.urls import include
from django.contrib.auth.models import User

from registro.api import UserAPI



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')),
    re_path(r'^api/v1/Primer/', include('Primer.urls')), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/1.0/create_user/', UserAPI.as_view(), name = "api_create_user")
]
