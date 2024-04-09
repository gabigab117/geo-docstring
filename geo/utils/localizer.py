import folium
from django.db.models import QuerySet

from account.models import CustomUser


def localize_users(users: QuerySet[CustomUser]):
    geo_map = folium.Map([48.866667, 2.333333])
    for user in users:
        folium.Marker([user.latitude, user.longitude]).add_to(geo_map)

    return geo_map
