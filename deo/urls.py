from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as deo_views

urlpatterns = [
    path('home/', deo_views.home, name='deo-page'),
]
