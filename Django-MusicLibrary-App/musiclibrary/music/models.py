# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    logo = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '{}-{}'.format(self.artist, self.title);

    def get_absolute_url(self):
        # return reverse('music:song_homepage', kwargs = {'pk':self.pk} )
        return reverse('music:song-homepage', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:song-homepage', kwargs={'pk': self.album.id})

    def __str__(self):
        return self.title
