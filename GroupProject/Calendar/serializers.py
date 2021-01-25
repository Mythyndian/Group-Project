from rest_framework import serializers
from .models import EventLog


class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ('id', 'data', 'application_user_id',
                  'import_events_id', 'comment_id',
                  'quest', 'title', 'note',
                  'created_at', 'checksum')


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ('quest', 'title', 'note')
