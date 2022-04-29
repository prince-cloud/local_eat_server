from django.db import models
from configuration.models import Tag
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

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class FoodType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type

class Food(models.Model):
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name='foods')
    type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=FOOD_SIZE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "".join(f"{self.resturant}  -   {self.name}")
