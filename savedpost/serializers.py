from rest_framework import serializers
from .models import SavedPost

class SavedPostSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        from posts.serializers import PostSerializer  
        post_serializer = PostSerializer(instance.post)
        return {
            'user': instance.user.username,
            'post': post_serializer.data,
            'saved_at': instance.saved_at,
            'is_saved_by_owner': instance.user == self.context['request'].user
        }

    class Meta:
        model = SavedPost
        fields = ['id', 'user', 'post', 'saved_at', 'is_saved_by_owner']