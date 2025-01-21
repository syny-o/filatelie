from django.contrib import admin
from .models import Profile, Address


admin.site.register(Address)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    