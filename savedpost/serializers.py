from rest_framework import serializers
from .models import SavedPost
from .serializers import PostSerializer

class SavedPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = PostSerializer()
    saved_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    is_saved_by_owner = serializers.SerializerMethodField()

    class Meta:
        model = SavedPost
        fields = ['id', 'user', 'post', 'saved_at', 'is_saved_by_owner']

    def get_is_saved_by_owner(self, obj):
        request = self.context.get('request')
        return obj.user == request.user
