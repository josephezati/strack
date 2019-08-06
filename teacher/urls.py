from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as teacher_views

urlpatterns = [
    path('home/', teacher_views.home, name='teacher-page'),
]
