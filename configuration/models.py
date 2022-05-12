from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tag

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name