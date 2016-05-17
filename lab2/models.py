from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)
    vocal = models.CharField(max_length=30)


class Discography(models.Model):
    album = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    songs = models.PositiveIntegerField()


class Clipography(models.Model):
    song = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    date = models.PositiveIntegerField()
    director = models.CharField(max_length=30)
