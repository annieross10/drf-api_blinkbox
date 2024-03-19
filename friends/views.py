from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Friend
from .serializers import FriendSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class FriendList(generics.ListCreateAPIView):
    """
    List all friend requests sent by the current user,
    i.e., all instances where the current user is the sender.
    Create a new friend request.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendSerializer

    def get_queryset(self):
        return Friend.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class FriendDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a friend request.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        # Allow deletion only if the current user is the sender
        if instance.sender == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"error": "You do not have permission to delete this friend request."},
                status=status.HTTP_403_FORBIDDEN
            )