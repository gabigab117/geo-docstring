from django.urls import path
from .views import map_view

app_name = "geo"

urlpatterns = [
    path("map/", map_view, name="map")
]
