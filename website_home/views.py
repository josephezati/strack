from django.shortcuts import render
def home(request):
	return render(request, 'website_home/home.html', {'title': 'Home'})

def schools(request):
	return render(request, 'website_home/schools.html', {'title': 'Schools'})

def teachers(request):
	return render(request, 'website_home/teachers.html', {'title': 'Teachers'})

def deos(request):
	return render(request, 'website_home/DEOs.html', {'title': 'DEOs'})

def resources(request):
	return render(request, 'website_home/resources.html', {'title': 'Resourcese'})

def marketing(request):
	return render(request, 'website_home/marketing.html', {'title': 'Marketing'})

def communication(request):
	return render(request, 'website_home/communication.html', {'title': 'Communication'})

def settings(request):
	return render(request, 'website_home/settings.html', {'title': 'Settings'})
