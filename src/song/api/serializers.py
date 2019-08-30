from rest_framework import serializers
from song.models import Song
from django.contrib.auth.models import User

class SongCreateUpdateSL(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = [
			'sid',
			'sname',
			'singer',
			'cost',
			#'desc',
		]


##############   URL GENERATOR FOR THE GIVEN POST   ###############

songs_list_url = serializers.HyperlinkedIdentityField(
	view_name='song-api:song_details',
	lookup_field='id'
	)


songs_delete_url = serializers.HyperlinkedIdentityField(
	view_name='song-api:song_delete',
	lookup_field='id'
	)

######################## .....  ########################

class SongListSL(serializers.ModelSerializer):
	url = songs_list_url
	class Meta:
		model = Song
		fields = [
			'sid',
			'sname',
			'singer',
			'cost',
			'desc',
			'url',
			'user',
		]

class SongDetailSL(serializers.ModelSerializer):
	url = songs_delete_url
	class Meta:
		model = Song
		fields = [
			'id',
			'sid',
			'sname',
			'singer',
			'cost',
			'desc',
			'url',
			'user',
		]		