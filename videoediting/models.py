from django.db import models

# Create your models here.
class Videoediting(models.Model):
    videos = models.FileField(upload_to='videos')
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Meta:
    ordering = ['id']
