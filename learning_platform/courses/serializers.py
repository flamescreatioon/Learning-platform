from rest_framework import serializers
from .models import Course, LectureMaterial


class LectureMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureMaterial
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    materials = LectureMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        
