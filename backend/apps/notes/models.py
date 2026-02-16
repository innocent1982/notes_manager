from django.db import models
from django.contrib.auth import get_user_model
from django.utils.http import MAX_HEADER_LENGTH

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True, unique=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    users = models.ManyToManyField(User)


class Lecture(models.Model):
    number = models.PositiveIntegerField(unique=True)
    file = models.FileField(upload_to="media/notes")
    uploaded_at = models.DateTimeField(blank=True)
    edited_at = models.DateTimeField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
