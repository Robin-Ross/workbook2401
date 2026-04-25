from rest_framework import serializers
from .models import Event, Talk

# TODO Part 2: Create EventSerializer using ModelSerializer for the Event model
#              Fields: id, name, description, location, start_date, end_date
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "name", "description", "location", "start_date", "end_date")
# TODO Part 3: Create TalkSerializer using ModelSerializer for the Talk model
#              Fields: id, event, title, description, speaker_name, status, scheduled_time
class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ("id", "event", "title", "description", "speaker_name", "status", "scheduled_time")
