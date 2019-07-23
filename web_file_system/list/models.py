from django.db import models

# Create your models here.
class image(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    path = models.TextField()
    type = models.TextField()
# max_length=1000
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__(self):
        return self.title
    