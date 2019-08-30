from django.urls import path
from .views import (
	player,
	song_entry,
	song_list_views,
	song_update_views,
	song_delete_views,
	extra_views,
	media_views
	)

app_name="song"

urlpatterns = [
path("entry/",song_entry,name="song_entry"),
path("show/",song_list_views,name="song_list"),
path("extra/",extra_views,name="extra"),
path("media/",media_views,name="media"),
path("update/<int:id>/",song_update_views,name="song_update"),
path("delete/<int:id>/",song_delete_views,name="song_delete"),
path('player/<int:id>/',player,name="players"),
]
