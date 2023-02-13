from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    monthly_listeners = models.IntegerField()


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    release_date = models.CharField(max_length=10)


class Song(models.Model):
    song_title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_length = models.IntegerField()
