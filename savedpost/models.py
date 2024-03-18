from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SavedPost(models.Model):
    """
    Model to store saved posts by users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('drf_api.Post', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(default=timezone.now)
    is_saved = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f"{self.user.username} saved {self.post.title}"

    @classmethod
    def save_post(cls, user, post):
        """
        Method to save a post for a user.
        """
        saved_post, created = cls.objects.get_or_create(user=user, post=post)
        if not created:
            saved_post.is_saved = True
            saved_post.save()

    @classmethod
    def unsave_post(cls, user, post):
        """
        Method to unsave a post for a user.
        """
        saved_post = cls.objects.filter(user=user, post=post).first()
        if saved_post:
            saved_post.is_saved = False
            saved_post.save()
