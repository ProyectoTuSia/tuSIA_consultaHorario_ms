from dataclasses import field
from rest_framework import serializers 
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Schedule
        fields = (
            'userId'
            'monday',
            'tuesday', 
            'wednesday' ,
            'thursday',
            'friday', 
            'saturday', 
        )