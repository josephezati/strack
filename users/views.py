from django.shortcuts import render,  redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(pk=settings.PUBLIC_GROUP_ID)
			user.groups.add(group)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Welcome {username} Your account has been created! Please login Now')
			
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def login_success(request):
	usergroup = None
	if request.user.is_authenticated:
		usergroup = request.user.groups.values_list('id', flat=True).last()
	if usergroup == settings.MINISTRY_GROUP_ID:
		return redirect('strack-home')
	elif usergroup == settings.DEO_GROUP_ID:
		return redirect('deo-page')
	elif usergroup == settings.TEACHER_GROUP_ID:
		return redirect('teacher-page')
	elif usergroup == settings.SCHOOL_GROUP_ID:
		return redirect('school-page')
	else:
		return redirect('website-home')
