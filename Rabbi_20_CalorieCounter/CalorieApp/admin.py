from django.contrib import admin
from .models import UserProfile, DailyConsumption

admin.site.register(UserProfile)
admin.site.register(DailyConsumption)
