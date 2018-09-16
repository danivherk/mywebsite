from django.db import models

class portfolio(models.Model):
        image = models.ImageField(upload_to= 'logos/')
        text = models.CharField(max_length=50)
