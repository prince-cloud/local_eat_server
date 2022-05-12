from rest_framework import serializers
from services import models as service_models
from django.contrib.auth import get_user_model
from configuration import models as configuration_models


User = get_user_model()


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuration_models.Tag
        fields = (
            "id",
            "tag",
        )

class FoodSerializer(serializers.ModelSerializer):
    #food_menu = FoodMenuSerializer()
    class Meta:
        model = service_models.Food
        fields = (
            "id",
            "name",
            "price",
            "description",
            "size",
            #"food_menu"
        )

class FoodMenuSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(read_only=True, many=True)
    class Meta:
        model = service_models.FoodMenu
        fields  = (
            "id",
            "resturant",
            "name",
            "image",
            "foods",
        )

class ResturantSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    #foods = FoodSerializer(read_only=True, many=True)
    food_menu = FoodMenuSerializer(read_only=True, many=True)
    class Meta:
        model = service_models.Resturant
        fields = (
            "id",
            "owner",
            "name",
            "image",
            "tags",
            #"foods",
            "food_menu",
            "date_created",
        )

class GroceriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_models.Groceries
        fields = (
            "id",
            "grocery_shop",
            "name",
            "category",
            "price",
            "description",
            "image",
        )

class GroceryShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_models.GroceryShop
        fields = (
            "id",
            "owner",
            "name",
            'image',
            "phone",
            "email",
            'location',
            'groceries',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = configuration_models.Category
        fields = (
            "id",
            "name",
        )