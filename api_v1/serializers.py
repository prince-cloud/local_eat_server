from dataclasses import field
from operator import mod
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


class ResturantSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    class Meta:
        model = service_models.Resturant
        fields = (
            "id",
            "owner",
            "name",
            "image",
            "tags",
            "date_created",
        )

