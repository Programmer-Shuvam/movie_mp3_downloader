from django.db import models

# Create your models here.


class bollywood(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField()
    desc = models.TextField()
    screenshot1 = models.ImageField()
    screenshot2 = models.ImageField()
    screenshot3 = models.ImageField()
    torrent = models.TextField()
    magnet = models.TextField()
    direct = models.TextField()


class hollywood(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField()
    desc = models.TextField()
    torrent = models.TextField()
    magnet = models.TextField()
    direct = models.TextField()


class music(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField()
    desc = models.TextField()
    direct = models.TextField()


class pcgames(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField()
    desc = models.TextField()
    torrent = models.TextField()
    direct = models.TextField()


class supersearch(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField()
    desc = models.TextField()
    screenshot1 = models.ImageField()
    screenshot2 = models.ImageField()
    screenshot3 = models.ImageField()
    torrent = models.TextField()
    magnet = models.TextField()
    direct = models.TextField()
