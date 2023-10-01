from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_upload = models.FileField(upload_to='videos/')
    transcript = models.TextField(blank=True)

    def __str__(self):
        return self.title