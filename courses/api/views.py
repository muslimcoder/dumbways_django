from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Courses
from ..seriazilers import CoursesSerializer

class CoursesViewSet(viewsets.ModelViewSet):

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filter_fields = ('title', 'price',)
