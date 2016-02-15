from rest_framework import serializers

from models import EventMain


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventMain
        fields = ('userid', 'eventid', 'event_title', 'event_status', 'event_start_dt', 'host_email')