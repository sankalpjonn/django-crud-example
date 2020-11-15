from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'last_udpated_on', 'is_active')
