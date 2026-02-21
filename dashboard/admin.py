from django.contrib import admin
from .models import SkillMatch

@admin.register(SkillMatch)
class SkillMatchAdmin(admin.ModelAdmin):
    list_display = ['user', 'matched_user', 'skill', 'status', 'created_at']
    list_filter = ['status', 'created_at']
