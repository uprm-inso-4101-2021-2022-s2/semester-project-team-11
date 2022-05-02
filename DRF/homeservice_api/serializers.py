from rest_framework import serializers
from homeservice.models import Job, Category

# Data we're sending acroos to React

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'time',
            'owner',
            'content',
            'price',
            'status'
        )