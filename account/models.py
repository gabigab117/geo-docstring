from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, latitude, longitude, password, **kwargs):
        if not email:
            raise ValueError("Un email doit être renseigné")
        if not username:
            raise ValueError("Username manquant")
        if not longitude:
            raise ValueError("Longitude manquant")
        if not latitude:
            raise ValueError("Latitude manquant")

        user = self.model(username=username, email=self.normalize_email(email), latitude=latitude, longitude=longitude,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, latitude, longitude, password, **kwargs):
        user = self.create_user(email, username, latitude, longitude, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    bio = models.CharField(max_length=50, blank=True)

    REQUIRED_FIELDS = ["username", "latitude", "longitude"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()
