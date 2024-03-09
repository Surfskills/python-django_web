from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
path("users/signup/", signup),
path("users/signin/", user_login),
path("users/forgot_password/", ForgotPasswordAPIView.as_view())
]
