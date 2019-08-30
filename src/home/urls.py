from django.urls import path
from .views import home_views
app_name='home'

urlpatterns =[

	path('', home_views,name="home"),

]
