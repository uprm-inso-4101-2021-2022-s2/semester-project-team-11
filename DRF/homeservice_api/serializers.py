from rest_framework import serializers
from homeservice.models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'owner',
            'content',
            'specialty',
            'price',
            'status'
        )