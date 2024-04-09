from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import render
from account.models import CustomUser


@login_required
def map_view(request):
    users: QuerySet[CustomUser] = CustomUser.objects.all()

    return render(request, "geo/map.html", context={"users": users})
