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

    @action(methods=["get"], detail=True, url_path="menu", url_name="resturant_menus")
    def resturant_menu(self, request, pk):
        resturant = get_object_or_404(service_models.Resturant, pk=pk)
        foods = resturant.food_menu.all()
        serializer = serializers.FoodMenuSerializer(
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

class FoodMenuViewSet(ModelViewSet):
    model = service_models.FoodMenu
    serializer_class = serializers.FoodMenuSerializer
    queryset = service_models.FoodMenu.objects.all()

    @action(methods=["get"], detail=True, url_path="foods", url_name="menu_foods")
    def menu_foods(self, request, pk):
        menu = get_object_or_404(service_models.FoodMenu, pk=pk)
        foods = menu.foods.all()
        serializer = serializers.FoodSerializer(
            foods, many=True, context=self.get_serializer_context()
        )
        return Response(data=serializer.data) 

class CategoriesViewSet(ModelViewSet):
    model = config_models.Category
    serializer_class = serializers.CategorySerializer
    queryset = config_models.Category.objects.all()


class GroceriesViewSet(ModelViewSet):
    model = service_models.Groceries
    serializer_class = serializers.GroceriesSerializer
    queryset = service_models.Groceries.objects.all()


class GroceryShopViewSet(ModelViewSet):
    model = service_models.GroceryShop
    serializer_class = serializers.GroceryShopSerializer 
    queryset = service_models.GroceryShop.objects.all()

    @action(methods=["get"], detail=True, url_path="groceries", url_name="grocery_shop_groceries")
    def menu_foods(self, request, pk):
        grocery_shop = get_object_or_404(service_models.GroceryShop, pk=pk)
        groceries = grocery_shop.groceries.all()
        serializer = serializers.GroceriesSerializer(
            groceries, many=True, context=self.get_serializer_context()
        )
        return Response(data=serializer.data) 
