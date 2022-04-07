from rest_framework import serializers
from homeservice.models import Job, ClientAccount, Category

# Data we're sending acroos to React
class ClientAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAccount
        fields = ('client_name', 'user_name', 'email', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'jobs')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'owner',
            'content',
            'price',
            'status'
        )