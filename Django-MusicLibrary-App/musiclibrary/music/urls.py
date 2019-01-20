from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
    # /music/ - Using Generic view
    url(r'^$', views.MusicHomepage.as_view(), name='music-homepage'),
    # music/<album_id>/  for example /music/123/ - Using Generic view
    url(r'^(?P<pk>[0-9+])/$', views.SongHomepage.as_view(), name='song-homepage'),
    # music/1/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.set_favourite_song, name='song-favourite'),
    # music/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='add-album'),
    # music/song/add/1
    url(r'^song/add/(?P<pk>[1-9]+)$', views.SongCreate.as_view(), name='add-song'),
    # music/album/edit/1
    url(r'^album/edit/(?P<pk>[1-9]+)$', views.AlbumEdit.as_view(), name='edit-album'),
    # music/album/delete/1
    url(r'^album/delete/(?P<pk>[1-9]+)$', views.AlbumDelete.as_view(), name='delete-album'),
]
