from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .models import Accounts
from .forms import AccountForm,LoginForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required
import json
import urllib


from django.contrib.auth import (
   
   authenticate,
   login,
   logout,
	
	)
# Create your views here.


def signup(request):
	form = AccountForm(request.POST or None)
	if form.is_valid():
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		username = request.POST['username']
		email    = request.POST['email']
		password = request.POST['password']
		if result['success']:
			user,create=User.objects.get_or_create(
				username=username,
				email=email,
			)
			user.set_password(password)
			user.save()	
			form.save()
			messages.success(request, 'New User added with success!')
			return redirect(reverse('accounts:signup'))
		else:
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			return redirect(reverse('accounts:signup'))
	else:
 		return render(request, 'accounts/signup.html', {'forms': form})


def login_view(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:

			user=authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				print(user)
				return redirect(reverse('home:home'))
			else:
				form = LoginForm()
				messages.error(request, 'User Name or password not matched')
				context = {
					
					'forms':form,
				}
				return render(request,'accounts/login.html',context)
		except:
			form = LoginForm()
			return render(request,'accounts/login.html',{'msg':'Error in login'})		
	else:
		form = LoginForm()
		return render(request,'accounts/login.html',{'forms':form})

@login_required
def logout_view(request):
	logout(request)
	return redirect(reverse('home:home'))


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        user = request.user
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('accounts:change_pass'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })






def user_view(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'accounts/user_list.html', { 'users': users })




def validate_username(request):
    username = request.GET.get('username')
    #print(username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    else:
    	data['correct_message'] = 'Username is Valid'    
    return JsonResponse(data)


def validate_email(request):
	email = request.GET.get('email')
	if  '@' in email and email[0] !='@':
		if '.'  in email:
			data={
			'is_wrong':''
			}
		else:
			data={
				'is_wrong':'Yes'
			}	
	else:
		data={
		'is_wrong':'Yes'
		}
	if data['is_wrong'] == "Yes":
		data['error_message']='Email must contain @ symbol and .'
	return JsonResponse(data)			

					