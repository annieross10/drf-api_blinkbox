from rest_framework import serializers
from .models import Friend
from django.db import IntegrityError

class FriendSerializer(serializers.ModelSerializer):
    """
    Serializer for the Friend model.
    Create method handles the unique constraint on 'sender' and 'receiver'.
    """
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver_name = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Friend
        fields = ['id', 'sender', 'receiver', 'created_at', 'receiver_name', 'accepted']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            sender = validated_data['sender']
            receiver = validated_data['receiver']
            friend_request = Friend.objects.filter(sender=sender, receiver=receiver).first()
            if friend_request:
                friend_request.accepted = False 
                friend_request.save()
                return friend_request
            else:
                raise serializers.ValidationError({'detail': 'Possible duplicate'})
