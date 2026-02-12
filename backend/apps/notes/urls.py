from django.urls import path
from apps.notes.serializers import CourseSerializer
from .views.course_views import CourseView
from .views.lecture_views import LectureView

urlpatterns = [
    path("course/create/", CourseView.as_view(), name="create-course"),
    path("course/get-courses/", CourseView.as_view(), name="get-courses"),
    path("course/update/<int:id>/", CourseView.as_view(), name="update-course"),
    path("course/delete/<int:id>/", CourseView.as_view(), name="delete-course"),
    path("lecture/get-lectures/", LectureView.as_view(), name="get-lectures"),
    path("lecture/get-lecture/", LectureView.as_view(), name="get-lecture"),
    path("lecture/create/", CourseView.as_view(), name="create-lecture"),
    path("lecture/update/", CourseView.as_view(), name="update-lecture"),
]
