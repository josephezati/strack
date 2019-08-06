from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.views.generic import (
	ListView,
	DetailView,
	UpdateView,
	CreateView
	)

from school_home.models import *

def home(request):
	all_schools = School.objects.count()
	all_deos = Deo.objects.count()
	all_teachers = Teacher.objects.count()
	all_resources = Resource.objects.count()
	all_trtransfer = TransferTeacher.objects.count()
	all_deotransfer = TransferDeo.objects.count()
	return render(request, 'teacher/home.html', {'title': 'Home', 
		'all_schools':all_schools, 
		'all_deos':all_deos, 
		'all_teachers':all_teachers, 
		'all_resources':all_resources, 
		'all_trtransfer':all_trtransfer, 
		'all_deotransfer':all_deotransfer })