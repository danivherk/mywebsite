from django.db import models



class Service(models.Model):
    image = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Meta:
    ordering = ['id']
