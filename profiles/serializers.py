from rest_framework import serializers
from .models import Profile
from friends.models import Friend


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friend_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_friend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            friend = Friend.objects.filter(
             sender=user, receiver=obj.owner
            ).first()
            return friend.id if friend else None
        return None


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'bio', 'birth_date', 'profile_picture', 'is_owner', 'friend_id', 
        ]


