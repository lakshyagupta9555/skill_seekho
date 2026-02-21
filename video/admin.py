from django.contrib import admin
from .models import VideoCall

@admin.register(VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    list_display = ['caller', 'receiver', 'status', 'started_at', 'duration']
    list_filter = ['status', 'started_at']
