# admin.py
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_picture', 'resume')  # Add 'resume' to the display list
    fields = ('name', 'profile_picture', 'resume')  # Allow resume upload in the admin form
