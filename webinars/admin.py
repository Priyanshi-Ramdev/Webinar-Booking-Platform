from django.contrib import admin
from .models import Webinar, Booking  # ✅ Import both models together
from django.db import models
from django.contrib.auth.models import User

class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker_name', 'date', 'time', 'category')
    list_filter = ('category', 'date')
    search_fields = ('title', 'speaker_name', 'description')

admin.site.register(Webinar)  # ✅ Register Webinar model

