# from django.http import JsonResponse, HttpResponse
# from django.core import serializers
# from django.shortcuts import get_list_or_404
# from ..models import Trip, Member, Itinerary
# from users.models import UserAccount

# import json

# def itinerary_get_handler(request, trip_id):
#     itinerary = get_list_or_404(Budget, trip=trip_id)
#     itinerary_json = serializers.serialize("json", itinerary)
#     return HttpResponse(itinerary_json, content_type="application/json")

# def itinerary_post_handler(request, trip_id):
    
#     data = json.loads(request.body)

#     """Delete user and use request.user"""
#     user = UserAccount.objects.get(id=1)

#     if not Member.objects.filter(trip=trip_id, member=user.pk).exists():
#         return JsonResponse(
#             {
#                 "status": "403",
#                 "message": f"You are not part of trip {trip_id}",
#             },
#             status=403,
#         )
#     else:
#         trip = Trip.objects.get(id=trip_id)

#         """Change user for request.user"""
#         newitinerary = Budget(
#             item=data["item"],
#             price=data["price"],
#             remark=data["remark"],
#             create_budget_user=user,
#             update_budget_user=user,
#             trip=trip,
#         )
#         new_itinerary.save()
#     return JsonResponse(
#         {"status": "201", "Budget": "Itinerary element successfully added to trip"}, status=201
#     )

# def itinerary_put_handler(request, trip_id):
#     return JsonResponse(
#         {'status':'OK',
#         'message':''
#         })

# def itinerary_delete_handler(request, trip_id):
    
#     data = json.loads(request.body)
#     # data = request.POST

#     if Itinerary.objects.filter(trip=trip_id, pk=data["item_id"]).exists():

#         item_to_delete = Itinerary.objects.get(trip=trip_id, id=data["item_id"])
#         item_to_delete.delete()

#         return JsonResponse(
#             {
#                 "status": "204",
#                 "message": f"Itinerary item successfully deleted from trip number {trip_id}",
#             },
#             status=204,
#         )
#     else:
#         return JsonResponse(
#             {"status": "404", "message": "Itinerary item does not exists"}, status=404
#         )
