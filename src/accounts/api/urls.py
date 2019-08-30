from django.urls import path
from .views import UserCreateAPIViews,UserNameGetterAPIView


app_name="accounts-api"

urlpatterns = [
path("login/",UserNameGetterAPIView.as_view(),name="login"),
path("register/",UserCreateAPIViews.as_view(),name="register"),

]
