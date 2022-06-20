from django.contrib import admin
from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
]