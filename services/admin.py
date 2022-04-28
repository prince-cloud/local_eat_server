from django.contrib import admin

# Register your models here.
from .models import Resturant, Tag
# Register your models here.
admin.site.register(Resturant)
admin.site.register(Tag)