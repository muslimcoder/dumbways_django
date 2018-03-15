from django.db import models

class Courses(models.Model):

    class Meta:
        db_table = "courses"

    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")
    video_url = models.CharField(max_length=128)
    price = models.FloatField(default=0)
    image_url = models.CharField(max_length=128, null=True, blank=True)
