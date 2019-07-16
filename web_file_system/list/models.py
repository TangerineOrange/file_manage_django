from django.db import models

# Create your models here.
class image(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    