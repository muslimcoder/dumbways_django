from rest_framework import viewsets

from ..models import Courses
from ..seriazilers import CoursesSerializer

class CoursesViewSet(viewsets.ModelViewSet):

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
