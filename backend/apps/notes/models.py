from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    users = models.ManyToManyField(User)


class Lecture(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.PositiveIntegerField(unique=True)
    file = models.FileField(upload_at="media/notes")
    uploaded_at = models.DateTimeField(blank=True)
    edited_at = models.DateTimeField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
