from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_list_or_404
from ..models import Member, Trip
from users.models import UserAccount
import json


def get_trip_members(request, trip_id):
    members = get_list_or_404(Member, trip=trip_id)
    members_json = serializers.serialize("json", members)
    return HttpResponse(members_json, content_type="application/json")


def member_post_handler(request, trip_id):

    data = json.loads(request.body)
    user = UserAccount.objects.get(id=1)

    if Member.objects.filter(trip=trip_id, member=data["user_id"]).exists():
        return JsonResponse(
            {
                "status": "403",
                "message": f"User already in trip {trip_id}",
            },
            status=403,
        )
    else:
        trip = Trip.objects.get(id=trip_id)
        new_member = UserAccount.objects.get(id=data["user_id"])

        """Change user for request.user"""
        new_member = Member(
            name=user.username,
            member=new_member,
            trip=trip,
            create_member_user=user,
            update_member_user=user,
        )

        new_member.save()       

        return JsonResponse(
            {
                "status": "201",
                "message": f"{user.username} succesfully joined trip {trip_id}",
            },
            
            status = 201,
        )


# Not needed for the app
def member_put_handler(request, trip_id):

    # user = request.user
    user = UserAccount.objects.get(id=1)
    data = json.loads(request.body)

    if Trip.objects.filter(pk=trip_id).exists():

        if Member.objects.filter(member=data["user_id"]).exists():

            if Member.objects.filter(member=user.id).exists():

                member_to_update = Member.objects.get(pk=data["user_id"])

                if "name" in data:
                    member_to_update.name = data["name"]

                    member_to_update.last_updated_by = user

                    member_to_update.save()

                    return JsonResponse(
                        {
                            "status": "204",
                            "message": f"Trip member {member_to_update.name} successfully updated",
                        },
                        status=204,
                    )
                else:
                    return JsonResponse(
                        {
                            "status": "100",
                            "message": f"No update: Request does not contain new values for existing datafields",
                        },
                        status=100,
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
                    "message": f"User is not a member of this trip",
                },
                status=404,
            )

    else:
        return JsonResponse(
            {
                "status": "403",
                "message": f"You're not the manager of this trip!",
            },
            status=403,
        )


def member_delete_handler(request, trip_id):

    data = json.loads(request.body)
    # data = request.POST
    print(data["user_id"])

    if Member.objects.filter(trip=trip_id, member=data["user_id"]).exists():
        member_to_delete = Member.objects.get(trip=trip_id, member=data["user_id"])

        member_name = member_to_delete.name
        member_to_delete.delete()

        return JsonResponse(
            {
                "status": "204",
                "message": f"Member  {member_name} successfully  deleted from trip number {trip_id}",
            },
            status=204,
        )
    else:
        return JsonResponse(
            {
                "status": "404",
                "message": f"Member not in trip number",
            },
            status=404,
        )
