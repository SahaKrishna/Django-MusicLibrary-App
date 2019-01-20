# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.template import loader
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView


class MusicHomepage(ListView):
    model = models.Album
    template_name = 'music/albumIndex.html'
    context_object_name = 'all_albums'
    queryset = models.Album.objects.all()


class SongHomepage(DetailView):
    model = models.Album
    template_name = 'music/songPage.html'

    def get_context_data(self, **kwargs):
        context = super(SongHomepage, self).get_context_data(**kwargs)
        context['all_songs_in_album'] = models.Song.objects.filter(album=self.kwargs['pk'])
        return context


def set_favourite_song(request, album_id):
    song_id = request.POST[
        "song"]
    try:
        album = models.Album.objects.get(pk=album_id)
        all_songs_in_album = album.song_set.all()
        # all_songs_in_album = models.Song.filter(album=album_id) # Its another way to Get Song Objects
        song = album.song_set.get(pk=song_id)

        # Update the Song Favourite Flag
        song.favourite = True
        song.save()

        # Now retrun to the same page
        template = loader.get_template('music/songPage.html')
        context = {
            'album': album,
            'all_songs_in_album': all_songs_in_album,
        }
        return HttpResponse(template.render(context, request))

    except album.DoesNotExist:
        raise Http404('Album Does not Exist')


class AlbumCreate(CreateView):
    model = models.Album
    fields = ['title', 'artist', 'logo', 'description']


class SongCreate(CreateView):
    model = models.Song
    fields = {'album', 'title', 'favourite'}

    def get_initial(self):
        initial = super(SongCreate, self).get_initial()
        # Here I am initializing the Album variable for Song
        initial['album'] = models.Album.objects.get(id=self.kwargs['pk'])
        return initial


class AlbumEdit(UpdateView):
    model = models.Album
    fields = ['title', 'artist', 'logo', 'description']


class AlbumDelete(DeleteView):
    model = models.Album
    success_url = reverse_lazy('music:music-homepage');
