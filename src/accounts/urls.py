from django.urls import path
from .views import (
	signup,
	login_view,
	logout_view,
	validate_username,
	validate_email,
	user_view,
	change_password,
	)

app_name="accounts"

urlpatterns=[
path('signup/',signup,name="signup"),
path('login/',login_view,name="login_view"),
path('logout/',logout_view,name="logout_view"),
path('userlist/',user_view,name="user_list"),
path('changepass/',change_password,name="change_pass"),
path('ajax/validate_username/', validate_username, name='validate_username'),
path('ajax/validate_email/', validate_email, name='validate_email'),
]