import pstats
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from datetime import datetime
from ..outgoing_api.placesAPI import get_trip_places
from ..models import Trip, Member
from users.models import UserAccount
import json
from datetime import datetime


def trip_get_handler(request):
    
    trips = get_list_or_404(Trip)
    trips_json = serializers.serialize("json", trips)
    return HttpResponse(trips_json, content_type="application/json")


def trip_post_handler(request):

    # user = request.user
    user = UserAccount.objects.get(id=1)

    """Deploy: json.loads... / Test: request.POST"""
    data = json.loads(request.body)
    # data = request.POST

    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")

    end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")

    new_trip = Trip(
        name=data["name"],
        creator=user,
        origin=data["origin"],
        destination=data["destination"],
        start_date=start_date,
        end_date=end_date,
        last_updated_by=user,
    )
    new_trip.save()

    new_member = Member(
        name=user.username,
        member=user,
        trip=new_trip,
        create_member_user=user,
        update_member_user=user,
    )

    new_member.save()

    """Places API call. No longer needed"""

    # get_trip_places(new_trip, float(data["latitude"]), float(data["longitude"]))

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
        },
        status=204,
    )

def single_trip_put(request, trip_id):

    # user = request.user
    user = UserAccount.objects.get(id=1)
    data = json.loads(request.body)

    if Trip.objects.filter(pk=trip_id).exists():

        trip_to_update = Trip.objects.get(pk=trip_id)

        if Trip.objects.filter(pk=trip_id, creator=user).exists():

            if "name" in data:
                trip_to_update.name = data["name"]
            if "origin" in data:
                trip_to_update.origin = data["origin"]
            if "destination" in data:
                trip_to_update.destination = data["destination"]
            if "start_date" in data:
                start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
                trip_to_update.start_date = (start_date,)
            if "end_date" in data:
                end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")
                trip_to_update.end_date = (end_date,)

            trip_to_update.last_updated_by = user

            trip_to_update.save()

            return JsonResponse(
                {
                    "status": "204",
                    "message": f"Trip number {trip_id} successfully updated",
                },
                status=204,
            )

        else:

            return JsonResponse(
                {
                    "status": "403",
                    "message": f"You're not the manager of this trip!",
                },
                status=403,
            )

    return JsonResponse(
        {
            "status": "404",
            "message": f"This trip doesn't exists",
        },
        status=404,
    )
