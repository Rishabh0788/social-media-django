from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    content = models.TextField(
        max_length=1000
    )

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    likes = models.ManyToManyField(
        User,
        related_name="liked_posts",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-created_at"
        ]


    def __str__(self):

        return (
            self.author.username
            + " - "
            + self.content[:30]
        )


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField(
        max_length=300
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "created_at"
        ]


    def __str__(self):

        return (
            self.user.username
            + ": "
            + self.text[:30]
        )