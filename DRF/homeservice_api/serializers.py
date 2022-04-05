from rest_framework import serializers
from homeservice.models import Job

# Data we're sending acroos to React

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