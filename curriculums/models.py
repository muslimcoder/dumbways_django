from django.db import models
from django.contrib.auth.models import User

class Curriculums(models.Model):

    class Meta:
        db_table = "curriculums"

    # main fields
    title = models.CharField(max_length=128)
    attachment_url = models.CharField(max_length=128)
    type = models.CharField(max_length=64)

    # relation fields
    course = models.ForeignKey(
        'courses.Courses',
        on_delete=models.CASCADE,
        null=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title
