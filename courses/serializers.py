from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Courses
from user.serializers import UserSerializer
from curriculums.serializers import CurriculumsSerializerSimple

class CoursesSerializer(serializers.ModelSerializer):
    curriculums = CurriculumsSerializerSimple(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'video_url',
            'price',
            'image_url',

            'curriculums',
            'created_by',
        )


    def create(self, validated_data):
        created_by_id = validated_data.get("created_by_id")
        validated_data.pop("created_by_id", None)

        # Once you are done, create the instance with the validated data
        course = Courses(**validated_data)

        # relate with user
        user = User.objects.filter(id=created_by_id).first()
        course.created_by = user
        course.save()

        return course

class CoursesSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'video_url',
            'price',
            'image_url',

            'created_by',
        )
