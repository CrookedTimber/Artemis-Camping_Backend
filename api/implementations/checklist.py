from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from ..models import Trip, Member, Checklist
from users.models import UserAccount

import json


def checklist_get_handler(request, trip_id):
    checklist = get_list_or_404(Checklist, trip=trip_id)
    checklist_json = serializers.serialize("json", checklist)
    return HttpResponse(checklist_json, content_type="application/json")


def checklist_post_handler(request, trip_id):

    data = json.loads(request.body)

    """Delete user and use request.user"""
    # user = UserAccount.objects.get(id=1)
    user = request.user

  

    if not Member.objects.filter(trip=trip_id, member=user.pk).exists():
        return JsonResponse(
            {
                "status": "403",
                "message": f"You are not part of trip {trip_id}",
            },
            status=403,
        )
    else:
        trip = Trip.objects.get(id=trip_id)

        """Change user for request.user"""
        new_checklist = Checklist(
            # name=user.email,
            item=data["item"],
            remark=data["remark"],
            user_in_charge=user,
            create_checklist_user=user,
            update_checklist_user=user,
            trip=trip,
        )
        new_checklist.save()
    return JsonResponse(
        {"status": "201", "message": "Checklist element successfully added to trip"}, status=201
    )


def checklist_put_handler(request, trip_id):
    return JsonResponse({"status": "OK", "message": ""})


def checklist_delete_handler(request, trip_id):

    data = json.loads(request.body)
    # data = request.POST

    if Checklist.objects.filter(trip=trip_id, pk=data["item_id"]).exists():

        item_to_delete = Checklist.objects.get(trip=trip_id, id=data["item_id"])
        item_to_delete.delete()

        return JsonResponse(
            {
                "status": "204",
                "message": f"Checklist item successfully deleted from trip number {trip_id}",
            },
            status=204,
        )
    else:
        return JsonResponse(
            {"status": "404", "message": "Checklist item does not exists"}, status=404
        )

    return JsonResponse({"status": "OK", "message": ""})
