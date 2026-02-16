from shutil import register_archive_format
from rest_framework import serializers
from .models import Course
from .models import Lecture
from apps.notes.utils.utility_serializers import (
    UtilityCourseSerializer,
    UtilityUserSerializer,
)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]

    def validate_name(self, value):
        if isinstance(value, str):
            return value
        return serializers.ValidationError("Course name must be string")


class LectureSerializer(serializers.ModelSerializer):
    course = UtilityCourseSerializer(read_only=True)
    user = UtilityUserSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ["id", "user", "number", "file", "course"]
