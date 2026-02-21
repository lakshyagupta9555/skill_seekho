from django.db import models
from django.contrib.auth.models import User
from users.models import Skill

class SkillMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_sent')
    matched_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_received')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.matched_user.username} ({self.skill.name})'

    class Meta:
        ordering = ['-created_at']
