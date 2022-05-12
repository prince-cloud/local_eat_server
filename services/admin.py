from django.contrib import admin

# Register your models here.
from .models import Resturant, FoodMenu, Food, Groceries, GroceryShop
# Register your models here.
admin.site.register(Resturant)
admin.site.register(FoodMenu)
admin.site.register(Food)
admin.site.register(GroceryShop)
admin.site.register(Groceries)