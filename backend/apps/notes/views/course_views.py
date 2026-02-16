from typing import List
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)
from apps.notes.serializers import CourseSerializer
from apps.notes.models import Course
from apps.notes.services.course_services.create_course import CreateCourse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CourseView(
    GenericAPIView,
    DestroyModelMixin,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = CourseSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        elif self.request.method == "GET":
            return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        if self.request.user:
            return Course.objects.filter(users=self.request.user)
        return Course.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        try:
            id = self.kwargs.get("id")
        except Exception as e:
            return Response(
                {
                    "message": f"Encountered the following id when retreiving lookup field: {str(e)}"
                },
                status=400,
            )
        instance = get_object_or_404(queryset, id=id)
        return instance

    def perform_create(self, validated_data):
        course_object = CreateCourse(validated_data)
        created, message = course_object.perform_create()
        if created:
            return Response({"message": message}, status=201)
        return Response({"message": message}, status=400)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(
            {"message": "Successfully edited course", "data": data}, status=200
        )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
