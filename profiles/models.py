from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    FITNESS_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
    null=True,
    blank=True
)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    height = models.FloatField(
        help_text="Height in cm",
        null=True,
        blank=True
    )

    weight = models.FloatField(
        help_text="Weight in kg",
        null=True,
        blank=True
    )

    fitness_level = models.CharField(
        max_length=20,
        choices=FITNESS_LEVEL_CHOICES
    )

    fitness_goal=models.CharField(
        max_length=100,
        blank=True
    )

    medical_conditions=models.TextField(
        blank=True
    )

    bio=models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )



    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"