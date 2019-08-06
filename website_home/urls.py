from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('schools/', views.schools, name='website-schools'),
    path('teachers/', views.teachers, name='website-teachers'),
    path('DEOs/', views.deos, name='website-deos'),
    path('resources/', views.resources, name='website-resources'),
    path('marketing/', views.marketing, name='website-marketing'),
    path('communication/', views.communication, name='website-communication'),
    path('settings/', views.settings, name='website-settings'),
]
