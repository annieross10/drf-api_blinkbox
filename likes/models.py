from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    LIKE = 'LIKE'
    LOVE = 'LOVE'
    LAUGH = 'LAUGH'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (LAUGH, 'Laugh'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE,  # Specify related_name here
    )
    created_at = models.DateTimeField(auto_now_add=True)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post} - {self.reaction_type}'