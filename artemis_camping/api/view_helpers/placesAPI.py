import googlemaps
from dotenv import load_dotenv

import os

load_dotenv()

from ..models import Place

# Create your views here.
print("running")

API_KEY = os.environ.get("API_KEY")

# lat = 54.40062359224829
# lon = -1.734956949889292
gmaps = googlemaps.Client(key=API_KEY)


def get_trip_places(trip, lat, lon):
    """_summary_
    Gathers data of several types of places near a trip destination point and stores them into the database.

    Args:
        trip (_type_): id of a Trip
        lat (_type_): Latitude of a trip destination point
        lon (_type_): Longitude of a trip destination point

    """
    campground = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1500, type="campground"
    )

    rv_park = gmaps.places_nearby(location=f"{lat},{lon}", radius=1500, type="rv_park")

    lodging = gmaps.places_nearby(location=f"{lat},{lon}", radius=1500, type="lodging")

    park = gmaps.places_nearby(location=f"{lat},{lon}", radius=1500, type="park")

    tourist_attraction = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="tourist_attraction"
    )

    parking = gmaps.places_nearby(location=f"{lat},{lon}", radius=1000, type="parking")

    bus_station = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="bus_station"
    )

    gas_station = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="gas_station"
    )

    train_station = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="train_station"
    )

    light_rail_station = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="light_rail_station"
    )

    subway_station = gmaps.places_nearby(
        location=f"{lat},{lon}", radius=1000, type="subway_station"
    )
    # police = gmaps.find_place("restaurant", "invalid")

    # hospital = gmaps.find_place("restaurant", "invalid")

    places_categories_list = [
        campground,
        rv_park,
        lodging,
        park,
        tourist_attraction,
        parking,
        bus_station,
        gas_station,
        train_station,
        light_rail_station,
        subway_station,
    ]

    categories_string_list = [
        "campground",
        "rv_park",
        "lodging",
        "park",
        "tourist_attraction",
        "parking",
        "bus_station",
        "gas_station",
        "train_station",
        "light_rail_station",
        "subway_station",
    ]

    categories_filters = []
    counter = 0

    for place_type in places_categories_list:

        for place in place_type["results"]:

            for type in place["types"]:

                if type not in categories_filters:

                    Place.objects.create(
                        name=place["name"],
                        type=categories_string_list[counter],
                        latitude=place["geometry"]["location"]["lat"],
                        longitude=place["geometry"]["location"]["lng"],
                        place_id=place["place_id"],
                        trip=trip,
                    )

        categories_filters.append(categories_string_list[counter])
        counter += 1