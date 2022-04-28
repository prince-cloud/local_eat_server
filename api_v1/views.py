from http.client import ResponseNotReady
from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import permissions as rest_permissions

from configuration import models as config_models
from services import models as service_models
from . import serializers
from . import permissions
# Create your views here.

class ResturantViewSet(ModelViewSet):
    model = service_models.Resturant
    serializer_class = serializers.ResturantSerializer
    queryset = service_models.Resturant.objects.all() 

class TgagsViewSet(ModelViewSet):
    model = config_models.Tag
    serializer_class = serializers.TagsSerializer
    queryset = config_models.Tag.objects.all() 