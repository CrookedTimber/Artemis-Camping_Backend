import pstats
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from datetime import datetime
from ..outgoing_api.placesAPI import get_trip_places
from ..models import Trip, Member


def trip_get_handler(request):
    trips = get_list_or_404(Trip)
    trips_json = serializers.serialize("json", trips)
    return HttpResponse(trips_json, content_type="application/json")


def trip_post_handler(request):

    user = request.user
    
    """Deploy: json.loads... / Test: request.POST"""
    data = json.loads(request.body)
    # data = request.POST

    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")

    end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")

    new_trip = Trip(
        name=data["name"],
        creator=user,
        destination_latitude=float(data["latitude"]),
        destination_longitude=float(data["longitude"]),
        start_date=start_date,
        end_date=end_date,
        last_updated_by=user,
    )
    new_trip.save()

    new_member = Member(
        name=user.email,
        member=user,
        trip=new_trip,
        create_member_user=user,
        update_member_user=user,
    )

    new_member.save()

    """Re-Enable on Deployment: Adds nearby Places to the database"""

    get_trip_places(new_trip, float(data["latitude"]), float(data["longitude"]))

    return JsonResponse(
        {
            "status": "201",
            "message": "Trip succesfully added to the database",
            "name": data["name"],
            "id": new_trip.pk,
        },
        status=201,
    )


def single_trip_get(request, trip_id):

    trip = get_list_or_404(Trip, id=trip_id)

    trip_json = serializers.serialize("json", trip)

    return HttpResponse(trip_json, content_type="application/json")


def single_trip_delete(request, trip_id):

    trip_to_delete = get_list_or_404(Trip, id=trip_id)
    # trip_to_delete = Trip.objects.get(id=trip_id)
    trip_to_delete.delete()

    return JsonResponse(
        {
            "status": "204",
            "message": f"Trip number {trip_id} successfully deleted",
        }, status=204
    )


def trip_put_handler(request):
    return JsonResponse({"status": "OK", "message": ""})
