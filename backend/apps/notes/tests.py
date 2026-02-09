from rest_framework.test import APIClient, APITestCase
from .models import Course
from django.urls import reverse
from rest_framework import status
from datetime import datetime


class TestCourse(APITestCase):
    def setUp(self):
        self.client_one = APIClient()
        self.client_two = APIClient()
        self.course_one = Course.objects.create(name="OOP", created_at=datetime.now())
        self.course_two = Course.objects.create(
            name="Machine Learning", created_at=datetime.now()
        )
        self.course_three = Course.objects.create(
            name="Software Engineering", created_at=datetime.now()
        )

    def test_create(self):
        url = reverse("create-course")
        payload = {"name": 2}
        response = self.client_one.post(url, payload, format="json")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_courses(self):
        url = reverse("get-courses")
        response = self.client_one.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())

    def test_update_course(self):
        url = reverse("update-course", kwargs={"id": 1})
        payload = {"name": "Graphics designing"}
        response = self.client_one.patch(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())

    def test_delete_course(self):
        url = reverse("delete-course", kwargs={"id": 2})
        response = self.client_one.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
