from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from ..models import Trip, Member, Checklist
from users.models import UserAccount
from datetime import datetime

import json


def checklist_get_handler(request, trip_id):  
    
    checklist = Checklist.objects.filter(trip=trip_id)
    checklist_json = serializers.serialize("json", checklist)
    return HttpResponse(checklist_json, content_type="application/json")


def checklist_post_handler(request, trip_id):

    data = json.loads(request.body)

    """Delete user and use request.user"""
    user = UserAccount.objects.get(id=1)
    # user = request.user

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
        
        user_in_charge = UserAccount.objects.get(id=data["person_in_charge"])

        """Change user for request.user"""
        new_checklist = Checklist(
            item=data["item"],
            remark=data["remark"],
            user_in_charge = user_in_charge,
            name = user_in_charge.username,
            create_checklist_user=user,
            update_checklist_user=user,
            trip=trip,
        )
        new_checklist.save()
    return JsonResponse(
        {"status": "201", "message": "Checklist element successfully added to trip"},
        status=201,
    )


def checklist_put_handler(request, trip_id):

    # user = request.user
    user = UserAccount.objects.get(id=1)
    data = json.loads(request.body)

    if Trip.objects.filter(pk=trip_id).exists():

        if Checklist.objects.filter(pk=data["item_id"]).exists():

            if Member.objects.filter(member=user.id).exists():

                checklist_to_update = Checklist.objects.get(pk=data["item_id"])

                if "item" in data:
                    checklist_to_update.item = data["item"]
                if "remark" in data:
                    checklist_to_update.remark = data["remark"]
                if "user_in_charge_id" in data:
                    new_user_in_charge = UserAccount.objects.get(
                        pk=data["user_in_charge_id"]
                    )
                    checklist_to_update.user_in_charge = new_user_in_charge

                checklist_to_update.update_checklist_user = user
                checklist_to_update.update_date = datetime.now()

                checklist_to_update.save()

                return JsonResponse(
                    {
                        "status": "201",
                        "message": f"Trip checklist successfully updated",
                    },
                    status=201,
                )

            else:
                return JsonResponse(
                    {
                        "status": "403",
                        "message": f"You are not a member of this trip",
                    },
                    status=403,
                )

        else:

            return JsonResponse(
                {
                    "status": "404",
                    "message": f"Item not part of the checklist in this trip",
                },
                status=404,
            )

    else:
        return JsonResponse(
            {
                "status": "404",
                "message": f"Trip does not exists",
            },
            status=403,
        )


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
