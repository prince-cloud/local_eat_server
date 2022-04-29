from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from configuration import models as config_models
from services import models as service_models
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# Create your views here.

class ResturantViewSet(ModelViewSet):
    model = service_models.Resturant
    serializer_class = serializers.ResturantSerializer
    queryset = service_models.Resturant.objects.all()

    @action(methods=["get"], detail=True, url_path="foods", url_name="resturant_foods")
    def resturant_foods(self, request, pk):
        resturant = get_object_or_404(service_models.Resturant, pk=pk)
        foods = resturant.foods.all()
        serializer = serializers.FoodSerializer(
            foods, many=True, context=self.get_serializer_context()
        )
        return Response(data=serializer.data) 

class TgagsViewSet(ModelViewSet):
    model = config_models.Tag
    serializer_class = serializers.TagsSerializer
    queryset = config_models.Tag.objects.all() 

class FoodsViewSet(ModelViewSet):
    model = service_models.Food
    serializer_class = serializers.FoodSerializer
    queryset = service_models.Food.objects.all()

class FoodTypeViewSet(ModelViewSet):
    model = service_models.FoodType
    serializer_class = serializers.FoodTypeSerializer
    queryset = service_models.FoodType.objects.all()