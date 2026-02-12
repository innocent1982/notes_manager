from rest_framework import serializers


class UtilityCourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500, read_only=True)


class UtilityUserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True, max_length=50)
