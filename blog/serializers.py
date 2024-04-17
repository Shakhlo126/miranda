from rest_framework import serializers
from .models import (Category,
                     Politics,
                     Health,
                     Sport,
                     Design,
                     Business)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politics
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']