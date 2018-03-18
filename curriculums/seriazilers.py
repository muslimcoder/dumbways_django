from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Curriculums
from courses.models import Courses
from user.serializers import UserSerializer
from courses.seriazilers import CoursesSerializer

class CurriculumsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)
    created_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    course = CoursesSerializer(required=False, read_only=True)
    course_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Curriculums
        fields = (
            'id',
            'title',
            'attachment_url',
            'type',

            'course_id',
            'course',
            'created_by_id',
            'created_by'
        )


    def create(self, validated_data):
        # Once you are done, create the instance with the validated data
        curriculum = Curriculums(**validated_data)

        # relate with user
        created_by_id = validated_data.get("created_by_id")
        validated_data.pop("created_by_id", None)
        user = User.objects.filter(id=created_by_id).first()
        curriculum.created_by = user

        # relate with course
        course_id = validated_data.get("course_id")
        validated_data.pop("course_id", None)
        course = Courses.objects.filter(id=course_id).first()
        curriculum.course = course

        curriculum.save()

        return curriculum
