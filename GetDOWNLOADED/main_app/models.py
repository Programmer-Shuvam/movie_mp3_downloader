from django.db import models
import datetime
# Create your models here.


class bollywood(models.Model):
    name = models.CharField(max_length=100)
    cover = models.TextField()
    desc = models.TextField()
    screenshot1 = models.TextField()
    screenshot2 = models.TextField()
    screenshot3 = models.TextField()
    torrent = models.TextField()
    magnet = models.TextField()
    direct = models.TextField()

    def __str__(self):
        return self.name


class hollywood(models.Model):
    name = models.CharField(max_length=100)
    cover = models.TextField()
    desc = models.TextField()
    screenshot = models.TextField()
    links = models.TextField()
    imdb = models.FloatField(default=10)
    duration = models.CharField(max_length=50, default='unavailable')
    rel_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.name


class music(models.Model):
    name = models.CharField(max_length=100)
    cover = models.TextField()
    desc = models.TextField()
    direct = models.TextField()

    def __str__(self):
        return self.name


class pcgames(models.Model):
    name = models.CharField(max_length=100)
    cover = models.TextField()
    desc = models.TextField()
    torrent = models.TextField()
    direct = models.TextField()

    def __str__(self):
        return self.name
