from rest_framework import serializers
from .models import *


class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ('id', 'data', 'application_user_id',
                  'import_events_id', 'comments_id',
                  'quest', 'title', 'note',
                  'created_at', 'checksum')

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ('quest', 'title', 'note')

class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('id', 'data', 'login',
                  'email', 'roles',
                  'first_name', 'last_name', 'token',
                  'password', 'created_at')

class CreateApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('login', 'email', 'first_name', 'last_name', 'password', 'created_at')
