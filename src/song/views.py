from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.urls import reverse
from .models import Song,Try
from .forms import SongForm,TryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def song_entry(request):
	form = SongForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		song = form.save(commit=False)
		song.user = request.user
		song.save()
		form = SongForm()
		context={
			'msg':"Successfully submitted"
		}
		return redirect(reverse('song:song_list'))
	context ={
		'forms':form,
	}

	return render(request,'song/song_entry.html',context)	

@login_required
def song_list_views(request):
	song_obj = Song.objects.all()
	#user_list = User.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(song_obj, 8)
	try:
		song_obj = paginator.page(page)
	except PageNotAnInteger:
		song_obj = paginator.page(1)
	except EmptyPage:
		song_obj = paginator.page(paginator.num_pages)
	songlist = []
	for i in song_obj:
		son = i
		songlist.append(son)
	print(songlist)	
	context={
		'song_obj':song_obj,
		'songlist':songlist,
		
	}
	return render(request,"song/show_list.html",context)		

@login_required
def song_update_views(request,id=None):
	song = Song.objects.get(id=id)
	auth_user=str(request.user.username)
	song_user=str(song.user)
	print(request.user.username,song.user)
	if auth_user == song_user:
		form = SongForm(request.POST or None,request.FILES or None, instance=song)
		if form.is_valid():
			form.save()
			form = SongForm()
			return redirect(reverse('song:song_list'))
		context={
			'forms':form,
			'song':song,
		
		}	
		# messages.success(request, 'You have permission to update it!')
		return render(request,'song/song_update.html',context)
	else:
		messages.error(request, 'You have no permission to update it!')
		return render(request,'song/song_update.html',{'song':song})	
			

@login_required
def song_delete_views(request,id=None):
	song = Song.objects.get(id=id)
	song.delete()
	return redirect(reverse('song:song_list'))

@login_required
def extra_views(request):
	form = TryForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		form.save()
		form = TryForm()
		context={
			'msg':"Successfully submitted"
		}
		return redirect(reverse('home:home'))
	context ={
		'forms':form,
	}

	return render(request,'song/extra.html',context)


@login_required
def media_views(request):
	instance = Try.objects.all()
	context = {
		'instance':instance,
		
	}
	return render(request,'song/image.html',context)		
@login_required
def player(request,id=None):
	song_obj = Song.objects.get(id=id)
	print(song_obj)
	context = {
		'songlist':song_obj,
	}	
	return render(request,'player/players.html',context)
