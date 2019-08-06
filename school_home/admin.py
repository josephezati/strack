from django.contrib import admin
from .models import *
from django.db import models
admin.site.register( School )
admin.site.register( Teacher )
admin.site.register( TransferTeacher )
admin.site.register( Product )