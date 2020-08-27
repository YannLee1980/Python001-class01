from django.urls import path
from . import views

urlpatterns = [
    path('index', views.log_in),
    path('login', views.log_in),
    path('', views.log_in),
]
