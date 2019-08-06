from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('website_home.urls')),
	path('users/', include('users.urls')),
	path('school_home/', include('school_home.urls')),
	path('school/', include('school.urls')),
	path('teacher/', include('teacher.urls')),
	path('deo/', include('deo.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
