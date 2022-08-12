from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from ..models import Trip, Member, Budget
from users.models import UserAccount
from datetime import datetime

import json


def budget_get_handler(request, trip_id):
    
    budget = Budget.objects.filter(trip=trip_id)
    budget_json = serializers.serialize("json", budget)
    return HttpResponse(budget_json, content_type="application/json")


def budget_post_handler(request, trip_id):

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

        new_budget = Budget(
            item=data["item"],
            price=data["price"],
            remark=data["remark"],
            create_budget_user=user,
            update_budget_user=user,
            trip=trip,
        )
        new_budget.save()
    return JsonResponse(
        {"status": "201", "Budget": "Checklist element successfully added to trip"},
        status=201,
    )


def budget_put_handler(request, trip_id):

    # user = request.user
    user = UserAccount.objects.get(id=1)
    data = json.loads(request.body)

    if Trip.objects.filter(pk=trip_id).exists():

        if Budget.objects.filter(pk=data["item_id"]).exists():

            if Member.objects.filter(member=user.id).exists():

                budget_to_update = Budget.objects.get(pk=data["item_id"])

                if "item" in data:
                    budget_to_update.item = data["item"]
                if "price" in data:
                    budget_to_update.price = data["price"]
                if "remark" in data:
                    budget_to_update.remark = data["remark"]

                budget_to_update.update_budget_user = user
                budget_to_update.update_date = datetime.now()

                budget_to_update.save()

                return JsonResponse(
                    {
                        "status": "201",
                        "message": f"Budget item successfully updated",
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
                    "message": f"Item not part of the budget in this trip",
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


def budget_delete_handler(request, trip_id):

    data = json.loads(request.body)

    if Budget.objects.filter(trip=trip_id, pk=data["item_id"]).exists():

        item_to_delete = Budget.objects.get(trip=trip_id, id=data["item_id"])
        item_to_delete.delete()

        return JsonResponse(
            {
                "status": "204",
                "message": f"Budget item successfully deleted from trip number {trip_id}",
            },
            status=204,
        )
    else:
        return JsonResponse(
            {"status": "404", "message": "Budget item does not exists"}, status=404
        )
