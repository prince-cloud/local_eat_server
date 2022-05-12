from unicodedata import category
from django.db import models
from configuration.models import Category, Tag
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

FOOD_SIZE = (
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("F S", "F S"),
)
class Resturant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="resturant")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resturants/')
    tags = models.ManyToManyField(Tag)
    location = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class FoodMenu(models.Model):
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='food_menu')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="menu/")

    def __str__(self) -> str:
        return ''.join(f'{self.name} - {self.resturant}')

class Food(models.Model):
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='foods')
    food_menu = models.ForeignKey(FoodMenu, on_delete=models.SET_NULL, null=True, related_name="foods")
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=FOOD_SIZE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "".join(f"{self.resturant}  -   {self.name}")



class GroceryShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="grocery_shop")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="GroceryShops/")
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Groceries(models.Model):
    grocery_shop = models.ForeignKey(GroceryShop, related_name="groceries", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="groceries", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='groceries/')
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name