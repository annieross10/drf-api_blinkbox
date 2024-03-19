from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    """
    Friend model, representing a friend request and acceptance between users.
    'sender' is a User instance who sends the friend request.
    'receiver' is a User instance who receives the friend request.
    'accepted' indicates whether the friend request has been accepted.
    'created_at' stores the timestamp when the friend request was sent.
    """
    sender = models.ForeignKey(
        User, related_name='sent_friend_requests', on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name='received_friend_requests', on_delete=models.CASCADE
    )
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['sender', 'receiver']

    def __str__(self):
        return f'{self.sender} sent friend request to {self.receiver}'