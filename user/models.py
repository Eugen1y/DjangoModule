from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    money = models.PositiveIntegerField(default=10_000)
