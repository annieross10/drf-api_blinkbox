from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like
from posts.models import Post


from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post.id')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post_id', 'created_at', 'reaction_type']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })