from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Abs


class User(AbstractUser):
    email = models.EmailField()
