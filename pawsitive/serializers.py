from rest_framework import serializers
from .models import Pet, AdoptionApplication

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'age', 'gender', 'description', 
                 'image', 'status', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at']

class AdoptionApplicationSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    
    class Meta:
        model = AdoptionApplication
        fields = ['id', 'pet', 'pet_name', 'name', 'phone', 'email', 
                 'address', 'reason', 'status', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at'] 