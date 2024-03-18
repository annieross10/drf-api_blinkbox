from rest_framework import serializers
from .models import Post
from profiles.serializers import ProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Post
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'created_at', 'content', 'title', 'likes', 'location', 'image']
        read_only_fields = ['created_at', 'likes']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user
