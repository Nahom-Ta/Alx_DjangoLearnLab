from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_following',  # Avoids clash with followers
        blank=True
    )

    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',  # Avoids clash with following
        blank=True
    )

    def follow(self, user):
        """Follow a user."""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user."""
        self.following.remove(user)

    def is_following(self, user):
        """Check if the current user is following another user."""
        return self.following.filter(id=user.id).exists()

    def __str__(self):
        return self.username

from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
