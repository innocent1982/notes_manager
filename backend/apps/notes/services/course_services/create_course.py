from apps.notes.models import Course
from datetime import datetime


class CreateCourse:
    def __init__(self, validated_data):
        self.data = validated_data

    def perform_create(self):
        try:
            Course.objects.create(**self.data, created_at=datetime.now())
            return True, "Successfully created Course"
        except Exception as e:
            return False, f"Failed to create course: {str(e)}"
