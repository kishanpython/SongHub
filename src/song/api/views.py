from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAdminUser,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)
from .permissions import IsOwnerOrReadOnly
from .serializers import SongCreateUpdateSL,SongListSL,SongDetailSL
from song.models import Song

class SongCreateAPIViews(CreateAPIView):
	queryset = Song.objects.all()
	serializer_class =  SongCreateUpdateSL
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class SongListAPIViews(ListAPIView):
	queryset = Song.objects.all()
	serializer_class =  SongListSL


class SongDetailAPIViews(RetrieveAPIView):
	queryset = Song.objects.all()
	serializer_class =  SongDetailSL
	lookup_field = 'id'
	

class SongUpdateAPIViews(RetrieveUpdateAPIView):
	queryset = Song.objects.all()
	serializer_class =  SongCreateUpdateSL
	lookup_field = 'id'
	permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	def perform_update(self, serializer):
		serializer.save(user = self.request.user)

class SongDeleteAPIViews(DestroyAPIView):
	queryset = Song.objects.all()
	serializer_class =  SongDetailSL
	lookup_field = 'id'

