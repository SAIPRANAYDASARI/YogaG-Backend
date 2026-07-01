from django.db import models
from categories.models import Category


class Video(models.Model):

    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='videos'
    )

    youtube_url = models.URLField()

    thumbnail = models.ImageField(
        upload_to='video_thumbnails/',
        blank=True,
        null=True
    )

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    focus_area = models.CharField(
    max_length=100,
    help_text="Example: Neck, Shoulders, Lower Back"
    )
    is_active = models.BooleanField(
    default=True
    )

    order = models.PositiveIntegerField(
        default=1,
        help_text="Order of video in a session"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    

class VideoBenefit(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='benefits'
    )

    benefit = models.TextField()

    order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.video.title} - Benefit {self.order}"
    
    
    
class VideoStep(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='steps'
    )

    step = models.TextField()

    order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.video.title} - Step {self.order}"