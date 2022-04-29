from django.contrib import admin

# Register your models here.
from .models import Resturant, FoodType, Food
# Register your models here.
admin.site.register(Resturant)
admin.site.register(FoodType)
admin.site.register(Food)