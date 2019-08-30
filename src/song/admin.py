from django.contrib import admin
from .models import Song,Try
# Register your models here.


class SongAdmin(admin.ModelAdmin):
	list_display=['sid','sname','singer','cost','desc','file']

class TryAdmin(admin.ModelAdmin):
	list_display=['gender','date','image']	

admin.site.register(Song,SongAdmin)
admin.site.register(Try,TryAdmin)
