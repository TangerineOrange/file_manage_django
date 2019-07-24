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

class Movies(models.Model):
    id = models.AutoField(primary_key=True)

    number = models.CharField(max_length=30)
    title = models.TextField()
    movie_path = models.TextField()
    cover_name = models.TextField()
    cover_path = models.TextField()
    stars = models.CharField(max_length=30)
    date = models.DateField()
    studio = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    series = models.TextField()
    # genre = models.TextField()

    def __str__(self):
        return self.number
