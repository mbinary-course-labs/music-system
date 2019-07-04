from django.db import models

from django.utils import timezone


class user(models.Model):
    userId = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    isVip = models.BooleanField(default=False)

    # passwd, avatar
    def __str__(self):
        return f'{self.userId}'


class artist(models.Model):
    artistId = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    desc = models.CharField(max_length=1000)
    def __str__(self):
        return f'{self.artistId}'


class album(models.Model):
    albumId = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    desc = models.CharField(max_length=1000)

    # relation
    artist = models.ManyToManyField(artist)

    def __str__(self):
        return f'{self.albumId}'

    # image


class music(models.Model):
    musicId = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    isVip = models.BooleanField(default=False)

    # relation
    album = models.ForeignKey(album, on_delete=models.SET_NULL, null=True)
    artist = models.ManyToManyField(artist)

    def __str__(self):
        return f'{self.musicId}'
