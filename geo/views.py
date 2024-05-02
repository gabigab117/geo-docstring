import folium
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import render
from account.models import CustomUser
from .utils import localize_users


def map_view(request):
    users: QuerySet[CustomUser] = CustomUser.objects.all()
    geo_map = localize_users(users)
    geo_map = geo_map._repr_html_()

    return render(request, "geo/map.html", context={"map": geo_map})
