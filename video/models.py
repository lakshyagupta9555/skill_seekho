from django.db import models
from django.contrib.auth.models import User

class VideoCall(models.Model):
    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calls_made')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calls_received')
    room_id = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0, help_text='Duration in seconds')
    status = models.CharField(max_length=20, choices=(
        ('calling', 'Calling'),
        ('active', 'Active'),
        ('ended', 'Ended'),
        ('missed', 'Missed'),
    ), default='calling')

    def __str__(self):
        return f'{self.caller.username} -> {self.receiver.username} ({self.status})'

    class Meta:
        ordering = ['-started_at']
