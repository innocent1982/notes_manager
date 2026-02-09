from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]

    def validate_name(self, value):
        if isinstance(value, str):
            return value
        return serializers.ValidationError("Course name must be string")
