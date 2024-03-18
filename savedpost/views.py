from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import SavedPost
from .serializers import SavedPostSerializer

class ListSavedPostsView(generics.ListAPIView):
    """
    API view to list saved posts for a user.
    """
    serializer_class = SavedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedPost.objects.filter(user=self.request.user)

class SavePostView(generics.CreateAPIView):
    """
    API view to save a post for a user.
    """
    serializer_class = SavedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UnsavePostView(generics.DestroyAPIView):
    """
    API view to unsave a post for a user.
    """
    queryset = SavedPost.objects.all()
    serializer_class = SavedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        saved_post = self.get_object()
        if saved_post.user == request.user:
            saved_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)