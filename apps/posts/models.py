from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=25
    )
    description = models.TextField()
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_owner'
    )

    def __str__(self):
        return str(self.id)


class PostImage(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_images'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_images'
    )

    def __str__(self):
        return str(self.id)
