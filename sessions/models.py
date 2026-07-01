from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from videos.models import Video

class Session(models.Model):

    STATUS_CHOICES = [
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

    total_videos = models.PositiveIntegerField(
        default=0
    )

    completed_videos = models.PositiveIntegerField(
        default=0
    )

    started_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='IN_PROGRESS'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.category.name}"
    




class SessionVideo(models.Model):

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='session_videos'
    )

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='session_videos'
    )

    completed = models.BooleanField(
        default=False
    )

    watched_duration = models.PositiveIntegerField(
        default=0,
        help_text="Watched duration in seconds"
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('session', 'video')
        ordering = ['id']

    def __str__(self):
        return f"{self.session.user.email} - {self.video.title}"