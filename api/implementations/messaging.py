from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from ..models import Trip, Member, Message
from users.models import UserAccount

import json


def get_trip_messages(request, trip_id):
    messages = get_list_or_404(Message, trip=trip_id)
    messages_json = serializers.serialize("json", messages)
    return HttpResponse(messages_json, content_type="application/json")


def messaging_post_handler(request, trip_id):

    data = json.loads(request.body)

    """Deploy: request.user / Test: user id=1"""
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

        """Deploy: request.user / Test: user id=1"""
        new_message = Message(
            name=user.email,
            message_body=data["message"],
            # create_message_user=user,
            create_message_user=request.user,
            trip=trip,
        )
        new_message.save()
    return JsonResponse(
        {"status": "201", "message": "Message successfully added to trip"}, status=201
    )


def message_delete_handler(request, trip_id):

    data = json.loads(request.body)

    if Message.objects.filter(trip=trip_id, pk=data["message_id"]).exists():

        message_to_delete = Message.objects.get(trip=trip_id, id=data["message_id"])
        message_to_delete.delete()

        return JsonResponse(
            {
                "status": "204",
                "message": f"Message successfully deleted from trip number {trip_id}",
            },
            status=204,
        )
    else:
        return JsonResponse(
            {"status": "404", "message": "Message does not exists"}, status=404
        )
