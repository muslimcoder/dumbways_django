from rest_framework import serializers

from .models import Courses
from user.serializers import UserSerializer

class CoursesSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)

    class Meta:
        model = Courses
        fields = ('__all__')
