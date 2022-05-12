from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()
router.register('resturants', views.ResturantViewSet)
router.register('tags', views.TgagsViewSet)
router.register('foods', views.FoodsViewSet)
router.register('food_menus', views.FoodMenuViewSet)
router.register('grocry_shop', views.GroceryShopViewSet)
router.register('categories', views.CategoriesViewSet)
router.register('groceries', views.GroceriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]