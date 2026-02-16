from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = [("Admin", "admin"), ("Student", "student")]
    email = models.EmailField()
    role = models.CharField(max_length=7, default="student", choices=ROLES)
