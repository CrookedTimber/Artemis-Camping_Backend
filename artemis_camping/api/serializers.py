from rest_framework import serializers
from .models import Trip



class TripSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    last_updated_by = serializers.ReadOnlyField(source="creator.username")
    
    class Meta:
        model = Trip
        fields = ["id", "name", "creator", "destination_latitude", "destination_longitude", "start_date", "end_date", "creation_date", "last_update", "last_updated_by", "public"]
    

