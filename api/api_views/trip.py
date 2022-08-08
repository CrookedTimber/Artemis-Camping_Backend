from rest_framework import generics, permissions
from ..models import Trip
from ..serializers import TripSerializer
from ..view_helpers.placesAPI import get_trip_places

class TripList(generics.ListAPIView):
    """Type: API View Class \n
    Lists all Trips in the Database 
    Authorization Needed: Admin"""

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAdminUser]
    
class TripCreate(generics.CreateAPIView):
    """Type: API View Class \n
    Creates a New Trip
    Authorization Needed: User"""
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
        
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
        


