from django.db import models
from configuration.models import Tag
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Resturant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="resturant")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resturants/')
    tags = models.ManyToManyField(Tag)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name