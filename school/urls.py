from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as school_views

urlpatterns = [
    path('home/', school_views.home, name='school-page'),
]
