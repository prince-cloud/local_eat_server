from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()
router.register('resturants', views.ResturantViewSet)
router.register('tags', views.TgagsViewSet)
router.register('foods', views.FoodsViewSet)
router.register('foodtypes', views.FoodTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]