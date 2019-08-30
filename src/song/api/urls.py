from django.urls import path
from .views import SongListAPIViews,SongDetailAPIViews,SongUpdateAPIViews,SongDeleteAPIViews,SongCreateAPIViews


app_name="song-api"

urlpatterns = [
path('',SongListAPIViews.as_view(),name="song_list"),
path('create/',SongCreateAPIViews.as_view(),name="create"),
path('<int:id>/',SongDetailAPIViews.as_view(),name="song_details"),
path('<int:id>/update/',SongUpdateAPIViews.as_view() ,name="song_update"),
path('<int:id>/delete/',SongDeleteAPIViews.as_view(),name="song_delete"),
]
