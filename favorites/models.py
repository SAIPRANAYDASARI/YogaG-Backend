from django.db import models
from django.contrib.auth.models import User
from videos.models import Video


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

        constraints = [
            models.UniqueConstraint(
                fields=["user","video"],
                name="unique_user_favorite",
            )
        ]

    def __str__(self):
        return f"{self.user.email} ❤️ {self.video.title}"