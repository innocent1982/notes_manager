from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from apps.notes.serializers import LectureSerializer
from apps.notes.models import Lecture
from django.shortcuts import get_list_or_404, get_object_or_404


class LectureView(
    GenericAPIView, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
):
    serializer_class = LectureSerializer
    lookup_field = "id"

    def get_object(self, *args, **kwargs):
        id = kwargs.get("id")
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=id)
        return obj

    def get_queryset(self):
        user = self.request.user
        queryset = get_list_or_404(Lecture, user=user)
        return queryset

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        return self.crate(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
