from django.urls import path, include
from rest_framework import routers

from restaurants.views import (
    RestaurantViewSet,
    MenuViewSet,
    VoteView,
    TodayMenuView,
    MostChosenMenuView,
)

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurants")
router.register("menus", MenuViewSet, basename="menus")


urlpatterns = [
    path("", include(router.urls)),
    path("votes/", VoteView.as_view(), name="create-vote"),
    path("today/", TodayMenuView.as_view(), name="menu-for-today"),
    path("results/", MostChosenMenuView.as_view(), name="results"),
]

app_name = "restaurants"
