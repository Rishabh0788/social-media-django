from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    bio = models.TextField(
        blank=True,
        max_length=300
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    followers = models.ManyToManyField(
        User,
        related_name="following",
        blank=True
    )

    def __str__(self):

        return self.user.username